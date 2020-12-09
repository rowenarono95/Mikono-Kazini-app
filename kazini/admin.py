 
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User,Employee,Employer,Job

# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Job)


admin.site.index_title="KAZINI"
admin.site.site_header="KAZINI Admin"
admin.site.site_title="MIKONO_KAZINI"