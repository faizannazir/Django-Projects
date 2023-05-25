from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

# Validators

def validate_not_after_today(value):
    if value > timezone.now().date():
        raise ValidationError("The date cannot be after today.")
    
def validate_at_least_18_years_old(value):
    today = timezone.now().date()
    delta = datetime.timedelta(days=18*365)
    if value > today - delta:
        raise ValidationError("User must be at least 18 years old.")



User._meta.get_field('username')._unique = False
User._meta.get_field('email')._unique = True
User.USERNAME_FIELD = 'email'
User.REQUIRED_FIELDS.remove('email')
User.REQUIRED_FIELDS.append('username')


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="employee")
    department = models.CharField(max_length=50)
    picture = models.ImageField()
    db_picture = models.BinaryField(verbose_name="Image_db",editable=True,null=True,blank=True)
    date_of_birth = models.DateField(validators=[validate_at_least_18_years_old])
    joining_date = models.DateField(validators=[validate_not_after_today])

    def __str__(self):
        return self.user.username
    
STATUS = (('Absent','ABSENT'),('Present',"PRESENT"))

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="attendance")
    date = models.DateField(auto_now_add=True)
    entrance_time = models.TimeField(null=True,blank=True)
    exit_time = models.TimeField(null=True,blank=True)
    total_time = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=10, blank=True,choices=STATUS)
    
    class Meta:
        # Add a unique constraint to ensure that each employee can have only one attendance entry per day
        unique_together = ('employee', 'date',)
        
    def __str__(self):
        return self.employee.user.username + ' - ' + str(self.date)

