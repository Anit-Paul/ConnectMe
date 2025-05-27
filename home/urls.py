from django.contrib import admin
from django.urls import path,include
from . views import homeAPI
urlpatterns = [
    path('', homeAPI.as_view(),name='homeAPI'),
]