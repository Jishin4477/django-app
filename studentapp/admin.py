# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Student,Teacher,Subject,Division
from . import models


# Register your models here.
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ("name", "address","place","division")



admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Division)
