from rest_framework import serializers
from .models import CustomUser


class UserSignUpSerializer(serializers.Serializer):
    
    password = serializers.CharField(max_length=100, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'full_name', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','email', 'full_name']