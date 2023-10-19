from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products',default='customerlogo.jpg')
    price = models.FloatField(help_text="price is in US $")
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(f"{self.name} - {self.createdDate.strftime('%d/%m/%y')}")