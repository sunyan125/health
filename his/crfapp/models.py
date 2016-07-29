from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, blank=True)
    depart = models.CharField(max_length=200, blank = True)
    cell = models.CharField(max_length=100, blank = True)

    def __unicode__(self):
        return self.user.username