# -*- coding: utf-8 -*-
 
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)



class Employer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)   

    def __str__(self):
        return self.user.username

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True) 

    
    def __str__(self):
        return self.user.username   
 
