from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import MyUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ['email', 'password']

class LogoutSerializer(serializers.Serializer):
    access = serializers.CharField()
    token = serializers.CharField()
    class Meta:
        # model = MyUser
        fields = ['access', 'refresh']