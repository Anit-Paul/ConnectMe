from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render
from social_features.models import Post,Follow
from authentication.models import MyUser
from authentication.serializers import userSerializer
from social_features.serializers import PostSerializers
from rest_framework.response import Response
from rest_framework import status
class homeAPI(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user=request.user
        posts=user.posts.all()
        all_user=MyUser.objects.exclude(email=user.email)
        return render(request, 'home/index.html', {'user': user, 'posts': posts,'follows':all_user})

class profileAPI(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = MyUser.objects.filter(email=request.user.email)
        posts = Post.objects.filter(author=request.user)
        return Response({
            "user": userSerializer(user, many=True).data,
            "posts": PostSerializers(posts, many=True).data
        })

class updateAPI(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = MyUser.objects.get(email=request.user.email)
        except MyUser.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = userSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data modified successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

