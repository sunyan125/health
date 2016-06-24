from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique = True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, blank=True)
    depart = models.CharField(max_length=200, blank = True)
    cell = models.CharField(max_length=100, blank = True)
#    loginTime = models.TimeField(blank=True)
#    lastLoginTime = models.TimeField(blank = True)

    def __unicode__(self):
        return self.username