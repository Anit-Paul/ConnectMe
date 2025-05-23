from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userSerializer
from django.contrib.auth import authenticate
class signin(APIView):
    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new user instance
            return Response({"data": serializer.data, "message": "Data saved successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    def post(self,request):
        email=request.data["email"]
        password=request.data["password"]
        user=authenticate(email=email,password=password)
        if user is not None:
            return Response({"message":"Login Successful"})
        else:
            return Response({"message":"Login failed"})