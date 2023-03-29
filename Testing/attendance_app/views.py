
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Employee, Attendance, User
from .forms import EmployeeRegistrationForm, EmployeeLoginForm,EmployeeUpdateForm
from .filters import AttendanceFilter,AdminAttendanceFilter





@login_required(login_url='login')
def register_employee(request):
    if request.user.is_superuser :
        form = EmployeeRegistrationForm()
        if request.method == 'POST':
            form = EmployeeRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # department = form.cleaned_data.get('department')
                # date_of_birth = form.cleaned_data.get('date_of_birth')
                # joining_date = form.cleaned_data.get('joining_date')
                # picture = form.cleaned_data.get('picture')
                # db_picture = picture.file.read()
                # employee = Employee.objects.create(
                # user=user, department=department, date_of_birth=date_of_birth, joining_date=joining_date, picture=picture,db_picture = db_picture)
                # employee.save()
                return redirect('home')
            else:
                for field_name, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field_name}: {error}")
        return render(request, 'attendance_app/register.html', {'form': form})
    else:
        return redirect('home')


@login_required(login_url='login')
def updateEmployee(request,pk):
    if request.user.is_superuser :
        employee = get_object_or_404(Employee,id=pk)
        # Employee.objects.get(id=pk)
        form = EmployeeUpdateForm(instance=employee)
        if request.method == 'POST':
            form = EmployeeUpdateForm(request.POST,request.FILES,instance=employee)
            if form.is_valid():
                    form.save()
                    return redirect('home')
            else:
                for field_name, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field_name}: {error}")
        context = {'form': form}
        return render(request, 'attendance_app/register.html',context=context)
    else:
        return redirect('home')
    


@login_required(login_url='login')
def delete(request,pk):
    if request.user.is_superuser :
        user = get_object_or_404(User,id=pk)
        # User.objects.get(id=pk)
        if request.method == "POST":
            if user.is_superuser:
                return HttpResponse("Can not delete Super user")
            user.delete()
            return redirect('home')
        context={'employee':user}
        return render(request, 'attendance_app/delete.html',context=context)
    else:
        return redirect('home')


def login_employee(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,"Invalid Creditionals ")
    else:
        form = EmployeeLoginForm()
    return render(request, 'attendance_app/accounts/signin.html', {'form': form})



@login_required(login_url='/login/')
def home(request):
    if request.user.is_superuser:
        employees = Employee.objects.all()
        # attendances = Attendance.objects.all()
        context = {'employees': employees,}
        return render(request, 'attendance_app/home.html', context)
    else:
        employee = get_object_or_404(Employee, user=request.user)
        # Employee.objects.get(user=request.user)
        # attendances = get_list_or_404(Attendance.objects.filter(employee=employee).order_by('-date'))
        # attendances = get_list_or_404(Attendance,employee=employee)
        attendances = Attendance.objects.filter(employee=employee).order_by('-date')
        context = {'employee': employee, 'attendances': attendances}
        return render(request, 'attendance_app/user/home.html', context)




@login_required(login_url='/login/')
def attendance(request):
    if request.user.is_superuser:
        attendances = Attendance.objects.all()
        filter = AdminAttendanceFilter(request.GET,attendances)
        attendances = filter.qs
        context = {
                   'attendanceRecord': attendances, 
                   'filter':filter}
        return render(request, 'attendance_app/attendances.html', context)
    else:
        employee = get_object_or_404(Employee, user=request.user)
        attendance = employee.attendance.all().order_by('-date')
        filter = AttendanceFilter(request.GET,attendance)
        attendance = filter.qs
        context = {'employee': employee,'filter':filter,'attendanceRecord':attendance}
        return render(request, 'attendance_app/user/attendance.html', context)

  

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('login')


























# @login_required(login_url='/login/')
# def profile(request):
#     if request.user.is_staff or request.user.is_superuser:
#         return redirect('home')
#     else:
#         employee = get_object_or_404(Employee, user=request.user)
#         context = {'employee': employee}
#         return render(request, 'attendance_app/user/profile.html', context)




# @login_required(login_url='/login/')
# def leave(request):
#     if request.user.is_staff or request.user.is_superuser:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             form = ApplyLeave(request.POST)
#             if form.is_valid():
#                 date = form.cleaned_data.get('date')
#                 reason = form.cleaned_data.get('reason')
#                 employee = get_object_or_404(Employee, user=request.user)
#                 form = Leave.objects.create(
#                     employee=employee, date=date, reason=reason)
#                 form.save()
#                 return redirect('home')
#         else:
#             context = {'form': ApplyLeave}
#         return render(request, 'attendance_app/applyleave.html', context)


# def loginForm(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == 'POST':
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     return render(request, 'attendance_app/accounts/signin.html',context={})
