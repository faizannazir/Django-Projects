from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='customers',default='customerlogo.jpg')


    def __str__(self) -> str:
        return str(self.name)