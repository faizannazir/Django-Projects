from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# Create your models here.

class Registeration(models.Model):
    IT = 'IT'
    MANAGEMENT = 'Management'
    DEPARTMENT_CHOICES =[
        (IT, 'Information Technology'),
        (MANAGEMENT, 'Management'),
    ]
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    image = models.ImageField(upload_to='mysqlapp/images/')
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Reg(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=24)

    def __str__(self):
        return self.name
    



# from .manager import CustomUserManager
    
# DEPARTMENT = [
#     ("IT","IT DEPARTMENT"),
#     ("HR","HR DEPARTMENT"),
#     ("CS","CS DEPARTMENT")
#     ]

    

# class User(AbstractBaseUser,PermissionsMixin):
#     id = models.AutoField(primary_key=True, unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(("email address"),unique=True)
#     department = models.CharField(max_length=255,choices=DEPARTMENT)
#     image = models.ImageField(upload_to='mysqlapp/profile_pics')
#     contact_no = models.CharField(max_length=15)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'department', 'image', 'contact_no']

