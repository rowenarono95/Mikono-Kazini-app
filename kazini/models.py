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

     
class Job(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    job_description = models.CharField(max_length=20)
    job_requirements = models.CharField(max_length=20)
    company_email = models.EmailField(max_length=255, unique=True)
  
 
