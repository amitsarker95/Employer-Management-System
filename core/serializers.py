from rest_framework import serializers
from django.conf import settings
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type' : 'password'} ,write_only = True)

    class Meta:

        model = CustomUser
        fields = ['full_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self, *args, **kwargs):
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        user = CustomUser.objects.filter(email= self.validated_data['email'])

        if password != password2:
            raise serializers.ValidationError({'error' : 'Password and confirm password are not the same'})
        if user.exists():
            raise serializers.ValidationError({'error' : 'This email already exists'})
        
        account = CustomUser.objects.create(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name']
            )
        account.set_password(password)
        account.save()

        return account
    

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','email', 'full_name']