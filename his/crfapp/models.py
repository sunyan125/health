from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, blank=True)
    depart = models.CharField(max_length=200, blank = True)
    cell = models.CharField(max_length=100, blank = True)

def __str__(self):
    return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

