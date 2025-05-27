from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from . serializers import FollowSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Follow
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
class followAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    def post(self, request):
        serializer = FollowSerializers(data=request.data)  # Corrected line
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        follows = Follow.objects.all()
        serializer = FollowSerializers(follows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
