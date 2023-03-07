from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from django.utils.translation import gettext_lazy as _
from .manager import CustumUserManager

DEPARTMENT = [
    ("IT","IT DEPARTMENT"),
    ("HR","HR DEPARTMENT"),
    ("CS","CS DEPARTMENT")
    ]

class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(_("email address"),unique=True)
    department = models.CharField(max_length=255,choices=DEPARTMENT)
    image = models.ImageField(upload_to='profile_pics')
    contact_no = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustumUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'department', 'image', 'contact_no']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

