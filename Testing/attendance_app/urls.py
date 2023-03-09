from django.urls import path
from . import views


# for image files 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register_employee,name='register'),
    # path('login/',views.login_employee,name='login'),
    path('login/',views.loginForm,name='login'),
    path('logout/',views.user_logout,name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)