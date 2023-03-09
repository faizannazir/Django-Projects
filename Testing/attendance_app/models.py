from django.db import models
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True
User.REQUIRED_FIELDS.remove('email')
User._meta.get_field('username')._unique = False
User.REQUIRED_FIELDS.append('username')
User.USERNAME_FIELD = 'email'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="employee")
    department = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures')
    date_of_birth = models.DateField()
    joining_date = models.DateField()

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="attendance")
    date = models.DateField(auto_now_add=True)
    entrance_time = models.TimeField(auto_now_add=True)
    exit_time = models.TimeField(null=True,blank=True)
    total_time = models.IntegerField(null=True,blank=True)
    
    class Meta:
        # Add a unique constraint to ensure that each employee can have only one attendance entry per day
        unique_together = ('employee', 'date',)
        
    def __str__(self):
        return self.employee.user.username + ' - ' + str(self.date)


# class Leave(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="leaves")
#     date = models.DateField()
#     reason = models.CharField(max_length=200)
#     approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.employee.user.username + ' - ' + self.reason