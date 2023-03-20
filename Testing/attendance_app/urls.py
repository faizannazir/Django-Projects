from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('attendance/',views.attendance,name='attendance'),
    path('register/',views.register_employee,name='register'),
    path('update/<str:pk>',views.updateEmployee,name='employee_update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('login/',views.login_employee,name='login'),
    path('logout/',views.user_logout,name='logout'),
    
]
