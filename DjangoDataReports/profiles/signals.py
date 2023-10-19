''' 
Two application senders and reciever on 
basis of notification from sender reciever perform
some actions here sender will be USER which will
notify that user is created then reciever Profile 
will create profile against that new USER
'''

from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,**kwargs):
    '''Created return true only once when user created'''
    if created:
        ''' Instance is new user which  is created '''
        Profile.objects.create(user = instance , bio = "new user created")


''' 
Override ready method in apps.py 
inside method 
        import profiles.signals
'''