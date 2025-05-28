from django.contrib import admin
from django.urls import path,include
from . views import followAPI,PostAPI
urlpatterns = [
    path('', followAPI.as_view(),name='followAPI'),
    path("post/",PostAPI.as_view(),name="postAPI")
]