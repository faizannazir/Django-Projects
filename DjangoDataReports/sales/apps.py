from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'
    '''override  ready function and add default_app_config in init file'''
    def ready(self):
        from .signals import calculate_total_price

# 

