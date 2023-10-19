from django.db import models
from products.models import Product
from profiles.models import Profile
from customers.models import Customer
from django.utils import timezone

from django.shortcuts import reverse

from .utils import generate_code
# Create your models here.

#  product times quantity will give price
class Position(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)
    
    def save(self,*args,**kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args,**kwargs)
    
    def get_sale_id(self):
        sale_obj = self.sale.first()
        return sale_obj.id

    def __str__(self) -> str:
        return f"id : {self.id}- product: {self.product}"
    

#  Sale can consist of many  position
class Sale(models.Model):
    transaction_id = models.CharField(max_length=150,blank=True)
    positions = models.ManyToManyField(Position,related_name='sale')
    total_price = models.FloatField(blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='sale')
    salesman = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sale')
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)


    def save(self,*args,**kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args,**kwargs)
    
    # all related positions to Sale object
    def get_positions(self):
        return self.positions.all()
    
    def __str__(self) -> str:
        return f"Sales for amount of $ {self.total_price}"
    
    def get_absolute_url(self):
        return reverse('sales:saleDetail',kwargs={"pk":self.pk})
    


class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.file_name}"