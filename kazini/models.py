# -*- coding: utf-8 -*-
 
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
