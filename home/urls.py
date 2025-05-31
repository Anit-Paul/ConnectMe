from django.contrib import admin
from django.urls import path,include
from . views import homeAPI,profileAPI,updateAPI
urlpatterns = [
    path('', homeAPI.as_view(),name='homeAPI'),
    path('profile/', profileAPI.as_view(),name='my_profile'),
    path('update/', updateAPI.as_view(),name='update_profile'),
]