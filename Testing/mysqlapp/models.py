from django.db import models
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