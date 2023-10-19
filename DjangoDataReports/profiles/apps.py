from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        import profiles.signals

''' 
Set default_app_config in init file to class ProfilesConfig 
default_app_config = 'profiles.apps.ProfilesConfig'
'''
