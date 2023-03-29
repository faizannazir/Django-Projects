from django.db import models
from django.contrib.auth.models import User



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
    date_of_birth = models.DateField()
    joining_date = models.DateField()

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

