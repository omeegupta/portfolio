from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("getproject/", views.getproject, name="getproject"),
    path("contactus/", views.contactus, name="contactus"),
  
]