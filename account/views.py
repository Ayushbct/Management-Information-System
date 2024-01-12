from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,SendPasswordResetEmailSerializer
from .serializers import UserPasswordResetSerializer
from .serializers import MyTokenObtainPairSerializer,UserViewSerializer
from .renderers import UserRenderer
from .models import User
from api.models import *
from api.serializers import *
from rest_framework import viewsets
##Generates token manually 
def get_tokens_for_user(user):
    refresh=MyTokenObtainPairSerializer.get_token(user)
    #refresh = RefreshToken.for_user(user)
   
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class UserRegistrationView(APIView):
    #queryset=User.objects.all()
    # serializer_class=[MyTokenObtainPairSerializer]
    #renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'msg':"Registration successful","token":token},status=status.HTTP_201_CREATED)

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    # serializer_class=[MyTokenObtainPairSerializer]
    #renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'msg':'Login Successful','token':token},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_error':['Email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET'])
def getUsers(request):
    users=User.objects.all()
    serializer=UserViewSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserHome(request):
    data = {
        '/user/register': 'User Registration',
        '/user/login': 'User Login',
        '/user/token': 'Token Generation',
        '/user/token/refresh/': 'Refresh Token',
        '/user/changepassword': 'Change Password',
        '/user/send-reset-password-email/':'Send Reset Email',
        '/user/getteacher/id':'Get teacher associated to a User by Id'
    }
    return Response(data)


class UserProfileView(APIView):
    #renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)


class UserChangePassword(APIView):
    #renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({
                'msg':'Password Changed successfully',
                },status=status.HTTP_200_OK)

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    #renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':"Password Reset link send.Please check your email"},status=status.HTTP_200_OK)

        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



class UserPasswordResetView(APIView):
    #renderer_class=[UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer=UserPasswordResetSerializer(data=request.data,context={"uid":uid,"token":token})
        if serializer.is_valid(raise_exception=True):
            return Response({
                'msg':"password reset successfully"

            },status=status.HTTP_200_OK)
        
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getTeacher(request,tid):
    user=User.objects.get(pk=tid)
    teacher= Teacher.objects.get(user=user)
    serializer=TeacherSerializer(teacher)
    return Response(serializer.data)


