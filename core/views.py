from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import UserSignUpSerializer, ProfileSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
    

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
