from django.conf.urls import url
from studentapp import views
urlpatterns = [
    url(r'^search/', views.get_all_students, name='search'),
    ]