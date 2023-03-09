
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Attendance, User
from .forms import EmployeeRegistrationForm, EmployeeLoginForm


@login_required(login_url='login')
def register_employee(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':
            form = EmployeeRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                department = form.cleaned_data.get('department')
                date_of_birth = form.cleaned_data.get('date_of_birth')
                joining_date = form.cleaned_data.get('joining_date')
                picture = form.cleaned_data.get('picture')
                employee = Employee.objects.create(
                    user=user, department=department, date_of_birth=date_of_birth, joining_date=joining_date, picture=picture)
                employee.save()
                login(request, user)
                return redirect('home')
        else:
            form = EmployeeRegistrationForm()
            return render(request, 'attendance_app/register.html', {'form': form})
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
        form = EmployeeLoginForm()
    return render(request, 'attendance_app/login.html', {'form': form})



def loginForm(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = EmployeeLoginForm()
    return render(request, 'attendance_app/accounts/signin.html',context={'form':form})


@login_required(login_url='/login/')
def home(request):
    if request.user.is_staff or request.user.is_superuser:
        employees = Employee.objects.all()
        attendances = Attendance.objects.all()
        admin = get_object_or_404(User, email=request.user)
        context = {'employees': employees,
                   'attendances': attendances, 'admin': admin}
        return render(request, 'attendance_app/adminhome.html', context)
    else:
        employee = get_object_or_404(Employee, user=request.user)
        # Employee.objects.get(user=request.user)
        # attendances = get_list_or_404(Attendance.objects.filter(employee=employee).order_by('-date'))
        # attendances = get_list_or_404(Attendance,employee=employee)
        attendances = Attendance.objects.filter(employee=employee).order_by('-date')
        context = {'employee': employee, 'attendances': attendances}
        return render(request, 'attendance_app/user/home.html', context)


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
    

@login_required(login_url='/login/')
def profile(request):
    if request.user.is_staff or request.user.is_superuser:
        employees = Employee.objects.all()
        attendances = Attendance.objects.all()
        admin = get_object_or_404(User, email=request.user)
        context = {'employees': employees,
                   'attendances': attendances, 'admin': admin}
        return render(request, 'attendance_app/adminhome.html', context)
    else:
        employee = get_object_or_404(Employee, user=request.user)
        context = {'employee': employee}
        return render(request, 'attendance_app/user/profile.html', context)


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('login')
