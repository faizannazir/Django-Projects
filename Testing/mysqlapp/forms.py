from django.forms import ModelForm

from .models import Registeration


class RegistrationForm(ModelForm):

    class Meta:
        model = Registeration
        fields = '__all__'