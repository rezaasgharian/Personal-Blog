from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('main', Main_Page, name='main'),
    path('cv', CV_Page, name='cv'),
]
