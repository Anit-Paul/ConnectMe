from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userSerializer
from django.contrib.auth import authenticate
from .models import MyUser
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

def signin(request):
    return render(request,'account/index.html')

def login(request):
    return render(request,'account/login.html')

def forget_password(request):
    return render(request,'account/forgetpassword.html')

def verify_otp(request):
    return render(request,'account/otp.html')

def set_new_password(request):
    return render(request,'account/newpassword.html')

def otp_verification(request):
    return render(request,'account/newpassword.html')
class signinAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        serializer = userSerializer(data=request.data)  # add files here
        if serializer.is_valid():
            serializer.save()  
            return Response({"data": serializer.data, "message": "Data saved successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class loginAPI(APIView):
    def post(self,request):
        email=request.data["email"]
        password=request.data["password"]
        user=authenticate(email=email,password=password)
        if user is not None:
            return Response({"message":"Login Successful"})
        else:
            return Response({"message":"Login failed"})
        
    def patch(self, request, *args, **kwargs):
        try:
            user = MyUser.objects.get(email=request.data.get("email"))
        except MyUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = userSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # <-- return here
        return Response(serializer.errors, status=400)  # <-- and return here