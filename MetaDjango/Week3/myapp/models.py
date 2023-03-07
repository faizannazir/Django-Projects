from django.db import models

# Create your models here.
DEPARTMENTS = [
    ("IT","IT DEPARTMENT"),
    ("managment","MANAGMENT DEPARTMENT"),
    ("finance","FINANCE DEPARTMENT")
]

class Account(models.Model):
    employee_id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    profile = models.ImageField()
    department = models.CharField(max_length=200 ,choices=DEPARTMENTS)
    contact = models.CharField(max_length=13)
