from django.db import models

# Create your models here.

class Notes(models.Model):
    heading = models.TextField(max_length=20)
    body = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.heading}"
    