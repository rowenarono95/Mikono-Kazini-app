# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
 
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from .models import *
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action, permission_classes as permission_decorator
from rest_framework.permissions import AllowAny

from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)




