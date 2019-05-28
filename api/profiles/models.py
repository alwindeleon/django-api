# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()


class PersonalProfile(models.Model):
    description = models.TextField()
    owner = models.ForeignKey('User', related_name='pprofile')

class WorkProfile(models.Model):
    description = models.TextField()
    author = models.ForeignKey('User', related_name='wprofile')