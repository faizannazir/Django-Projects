from django.urls import path

from .import views
app_name = 'myapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('class/',views.Home.as_view,name='Class'),
]