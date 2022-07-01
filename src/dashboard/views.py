from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    token_param_config = openapi.Parameter('Authorization', in_=openapi.IN_HEADER, description='', type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        return HttpResponse(self.request.user)