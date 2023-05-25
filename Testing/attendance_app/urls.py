from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('attendance/',views.attendance,name='attendance'),
    path('register/',views.register_employee,name='register'),
    path('update/<str:pk>/',views.updateEmployee,name='update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('login/',views.login_employee,name='login'),
    path('logout/',views.user_logout,name='logout'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
]
