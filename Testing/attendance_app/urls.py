from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('attendance/',views.attendance,name='attendance'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register_employee,name='register'),
    path('employeeupdate/<str:pk>',views.updateEmployee,name='employee_update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('login/',views.login_employee,name='login'),
    path('logout/',views.user_logout,name='logout'),
    
]
