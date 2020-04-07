"""jishinproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from studentapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create_student/', views.create_student, name='create'),
    url(r'^create_teacher/', views.create_teacher, name ='teacher'),
    url(r'^create_division/', views.create_division, name ='division'),
    url(r'^create_subject/', views.create_subject, name ='subject'),
    url(r'^student/', views.student, name='student'),
    url(r'^search/', views.get_all_students, name='search'),
    url('', include('studentapp.urls')),


]
