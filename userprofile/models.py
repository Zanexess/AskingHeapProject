# -*- coding:utf-8 -*-
from django.contrib.auth.models import AbstractUser
from loginApp.models import MyUserManager

from django.db import models

class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=40, null=True)
    middle_name = models.CharField(max_length=40, null=True)
    rate = models.IntegerField(default=0)

    objects = MyUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return self.username
