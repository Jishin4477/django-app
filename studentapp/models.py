# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    subject = models.ForeignKey(Subject, null=False)

    def __str__(self):
        return u'%s - %s' %(self.name, self.subject)

class Division(models.Model):
    name = models.CharField(max_length=20)

    teacher = models.ForeignKey(Teacher, null=True, related_name="teacher_class")

    def __str__(self):
        return u'%s - %s' %(self.name, self.teacher)

class Student(models.Model):

    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=40)
    division = models.ForeignKey(Division)

    def __str__(self):
        return u'%s-%s-%s' %(self.name,self.address,self.division)








