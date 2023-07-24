from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime


def validate_not_after_today(value):
    if value > timezone.now().date():
        raise ValidationError("The date cannot be after today.")
    
def validate_at_least_18_years_old(value):
    today = timezone.now().date()
    delta = datetime.timedelta(days=18*365)
    if value > today - delta:
        raise ValidationError("User must be at least 18 years old.")



class EmployeeRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.HiddenInput(),required=False)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    department = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True,validators=[validate_at_least_18_years_old], widget=forms.DateInput(attrs={'type':'date'}))
    joining_date = forms.DateField(required=True,validators=[validate_not_after_today] ,widget=forms.DateInput(attrs={'type':'date'}))
    picture = forms.ImageField(required=True)
    db_picture = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = AppUser
        fields = ('username','first_name', 'last_name','email', 'department','date_of_birth','joining_date','picture','password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.department = self.cleaned_data.get('department')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.joining_date = self.cleaned_data.get('joining_date')
        user.picture = self.cleaned_data.get('picture')
        user.db_picture = user.picture.file.read()
        user.username = f"{self.cleaned_data.get('first_name')}{self.cleaned_data.get('last_name')}"
        user.save()
        return user


class EmployeeLoginForm(forms.Form):
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'id':'user_email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'user_pass'}))



class EmployeeUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.HiddenInput(),required=False)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    department = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True,validators=[validate_at_least_18_years_old] ,widget=forms.DateInput(attrs={'type':'date'}))
    joining_date = forms.DateField(required=True, validators=[validate_not_after_today],widget=forms.DateInput(attrs={'type':'date'}))
    # picture = forms.ImageField(required=True,label="Image")

    class Meta:
        model = AppUser
        fields = ('username','email', 'first_name', 'last_name', 'department', 'date_of_birth', 'joining_date', 'picture')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = f"{self.cleaned_data.get('first_name')}{self.cleaned_data.get('last_name')}"
        if 'picture' in self.files:
            user.picture = self.files['picture']
            user.db_picture = self.cleaned_data['picture'].file.read()
        if commit:
            user.save()
        return user

