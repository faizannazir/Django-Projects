from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee



class EmployeeRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    department = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type':'date'}))
    joining_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type':'date'}))
    picture = forms.ImageField(required=True)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'department','date_of_birth','joining_date','picture','password1', 'password2')


class EmployeeLoginForm(forms.Form):
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'id':'user_email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'user_pass'}))



class EmployeeUpdateForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # department = forms.CharField(required=True)
    # date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type':'date'}))
    # joining_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type':'date'}))
    # picture = forms.ImageField(required=True,label="Image")

    class Meta:
        model = Employee
        fields = ('username','email', 'first_name', 'last_name', 'department', 'date_of_birth', 'joining_date', 'picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        self.fields['email'].initial = self.instance.user.email
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        user = self.instance.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        employee = super().save(commit=False)
        employee.user = user

        if 'picture' in self.files:
            employee.picture = self.files['picture']
            
        if commit:
            employee.save()
        return employee

