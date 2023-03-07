from django import forms
from django.forms import ModelForm

from .models import Account

#  Simple form from django 
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name:" , max_length=12)
    age = forms.IntegerField(label="Enter Your age:", max_value='100')
    email = forms.EmailField(label="Enter Your Email:",max_length=200)


class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    date = forms.DateField(widget=forms.widgets.NumberInput(attrs={'type':'date'}))
    favourite_dish_select = forms.ChoiceField(choices=[('italian','Italian'),('greek','Greek'),('turkish','Turkish')])
    favourite_dish_radio = forms.ChoiceField(widget=forms.widgets.RadioSelect(attrs={'width':'20px'}),choices=[('italian','Italian'),('greek','Greek'),('turkish','Turkish')])
    favourite_dish_checkbox = forms.ChoiceField(widget=forms.widgets.CheckboxSelectMultiple(attrs={'width':'20px'}),choices=[('italian','Italian'),('greek','Greek'),('turkish','Turkish')])
   

class SignupForm(ModelForm):

    class Meta:
        model = Account
        fields = '__all__'
