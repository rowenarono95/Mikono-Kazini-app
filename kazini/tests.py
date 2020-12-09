# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
 
from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.user = User(id=1,password='chela12345',email='chelangat@gmail.com',username='chela54',first_name='chelangat',last_name='rono')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        
    # Testing Save Method
    def test_save_method(self):
        self.user.save_user()
        user = User.objects.all()
        self.assertTrue(len(user) > 0)
        
    def test_delete_user(self):
        self.user.delete_user()
        user = User.objects.all()
        self.assertTrue(len(user)== 0) 
        
    def test_update_user(self):
        self.user.save_user()
        self.user.update_user(self.user.id, 'chelangat')
        changed_user = User.objects.filter(username ='chelangat')
        self.assertTrue(len(changed_user) > 0)       
