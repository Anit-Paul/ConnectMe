from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userSerializer
from django.contrib.auth import authenticate
from .models import MyUser
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from .mail import Mail
from rest_framework.authtoken.models import Token

class otpVerification:
    def __init__(self):
        self.send_otp=""
        self.email=""
    def verify_otp(self,request):
        self.email = request.POST.get('email')
        a=Mail()
        temp,self.send_otp=a.send_email(self.email)
        if temp:
            return render(request,'account/otp.html')
        else:
            return render(request,'account/forgetpassword.html')
    def otp_verification(self,request):
        otp=request.POST.get('otp')
        if otp==self.send_otp:
            request.session['email']=self.email
            return render(request,'account/newpassword.html')
        else:
            print("please enter the valid otp!")
            return render(request,'account/otp.html')
        
def signin(request):
    return render(request,'account/index.html')

def login(request):
    return render(request,'account/login.html')

def forget_password(request):
    return render(request,'account/forgetpassword.html')


def set_new_password(request):
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
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message":"Login Successful",'token':token.key})
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
    
class forgetPasswordAPI(APIView):
    def post(self, request):
        password = request.POST.get('password')
        c_password = request.POST.get('confirm_password')

        if password != c_password:
            return render(request, 'account/newpassword.html', {"error": "Passwords do not match"})

        email = request.session.get('email')  # Use get() to avoid KeyError

        if not email:
            print("Session has expired or email not found")
            return render(request, 'account/forgetpassword.html', {"error": "Session expired. Please try again."})

        try:
            user = MyUser.objects.get(email=email)
            # Update only the password
            serializer = userSerializer(user, data={"password": password}, partial=True)
            if serializer.is_valid():
                serializer.save()
                # Optional: clear session email after use
                request.session.pop('email', None)
                return Response({"message": "Password reset successfully"})
            return Response(serializer.errors, status=400)
        except MyUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
