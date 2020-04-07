# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import loader
from .models import Student, Division
from django.http import HttpResponse
from .models import Student, Division, Teacher, Subject
from .forms import studentForm, teacherform, divisionform, subjectform


def create_student(request):
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Saved the student</h1>')

    context = {
        'form': form
    }
    return render(request, 'user/create.html', context)


def create_teacher(request):
    form = teacherform()
    if request.method == 'POST':
        form = teacherform(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'user/teacher.html', context)


def create_division(request):
    form = divisionform()
    if request.method == 'POST':
        form = divisionform(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'user/division.html', context)


def create_subject(request):
    form = subjectform()
    if request.method == 'POST':
        form = subjectform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Saved...</h1>')

    context = {
        'form': form
    }
    return render(request, 'user/subject.html', context)


def student(request):
    obj = Student.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'user/form.html', context)


def get_all_students(request):
    query = request.GET.get('q')
    print(query)
    results = Student.objects.filter(name=query)
    student_in_div = Student.objects.filter(division__name='3A')
    print(student_in_div)
    for result in results:
        stud_sub = Student.objects.filter(division__teacher__subject__name=result.division.teacher.subject.name)
        print(stud_sub)
    context = {
        'results': results
    }
    return render(request, 'user/get.html', context)
