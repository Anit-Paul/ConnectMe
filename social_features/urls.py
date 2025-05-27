from django.contrib import admin
from django.urls import path,include
from . views import followAPI
urlpatterns = [
    path('', followAPI.as_view(),name='followAPI'),
]