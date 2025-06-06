"""
URL configuration for connectme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import signinAPI,loginAPI,signin,login,forget_password,set_new_password,otpVerification,forgetPasswordAPI,logoutAPI
otp=otpVerification()
urlpatterns = [
    path("",login,name="login"),
    path("signin/",signin,name="signin"),
    path("forget_password/",forget_password,name="forget_password"),
    path("verify_otp/",otp.verify_otp,name="verify_otp"),
    path("otp_verification/",otp.otp_verification,name="otp_verification"),
    path("forgetPassword/",forgetPasswordAPI.as_view(),name="forgetPassword"),
    path("set_new_password/",set_new_password,name="set_new_password"),
    path("signinAPI/",signinAPI.as_view(),name="signinAPI"),
    path("loginAPI/",loginAPI.as_view(),name="loginAPI"),
    path("logoutAPI/",logoutAPI,name="log_out")
]
