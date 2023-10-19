from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(default="nobio",max_length=120)
    avatar = models.ImageField(upload_to='avatars',default='customerlogo.jpg')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return str(f"Profile of {self.user.username}")