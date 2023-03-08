from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('leave/',views.leave,name='leave'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register_employee,name='register'),
    path('login/',views.login_employee,name='login'),
    path('logout/',views.user_logout,name='logout'),

]