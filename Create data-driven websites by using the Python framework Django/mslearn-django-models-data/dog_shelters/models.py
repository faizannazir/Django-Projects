from django.db import models

# Create your models here.
class Shelter(models.Model):
    id = models.BigAutoField(primary_key=True)  # explicitly define a primary key field
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f" name  = {self.name}"
    

class Dog(models.Model):
    id = models.BigAutoField(primary_key=True)  # explicitly define a primary key field
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    intake_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Dog = {self.name}"
    
    