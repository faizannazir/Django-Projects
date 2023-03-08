from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Leave

from django.utils import timezone

class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    department = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2003)))
    joining_date = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2021, 2024)))
    picture = forms.ImageField(required=True)
    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name','email', 'department','date_of_birth','joining_date','picture','password1', 'password2')

class EmployeeLoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ApplyLeave(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ('date','reason')

    widgets = {
        'date':forms.DateInput(attrs={type:'date','min':timezone.now().date,'value':timezone.now().date})
    }