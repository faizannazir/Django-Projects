from django.forms import ModelForm,forms

from .models import Registeration


class RegistrationForm(ModelForm):

    class Meta:
        model = Registeration
        fields = '__all__'


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            # check if email exists in database
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError(
                    'Invalid email or password.'
                )

            # set cleaned username to email
            self.cleaned_data['username'] = email

        return self.cleaned_data
