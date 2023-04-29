from django.db import models

# Create your models here.
class Images(models.Model):
    django_image= models.ImageField(verbose_name="Image")
    db_image = models.BinaryField(verbose_name="Image_db",editable=True)
