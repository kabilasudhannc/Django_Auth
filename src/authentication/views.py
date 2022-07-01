from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, LogoutSerializer
# from rest_framework import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt import exceptions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(APIView):
    register_serializer = RegisterSerializer

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LogoutView(APIView):
    # swagger_schema = None

    @swagger_auto_schema(request_body=LogoutSerializer)
    def post(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response({
                'detail': 'user logged out successfully',
                'code': 'success',
            })

        except exceptions.TokenError:
            return Response({
                "detail": "Token is invalid or expired",
                "code": "token_not_valid"
            })



