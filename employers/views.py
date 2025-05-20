from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import EmployerSerializer
from .models import Employer
from .permissions import EmployeOwnerOrReadOnly



class EmployerViewSet(ViewSet):

    permission_classes = [IsAuthenticated, EmployeOwnerOrReadOnly]

    def list(self, request):
        queryset = Employer.objects.all()
        serializer = EmployerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Employer.objects.all()
        employer = get_object_or_404(queryset, pk=pk)
        serializer = EmployerSerializer(employer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request):
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        try:
            employer = Employer.objects.get(pk=pk)
        except Employer.DoesNotExist:
            return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployerSerializer(employer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        platform = Employer.objects.get(pk=pk)
        platform.delete()
        return Response({'delete': "Object has been deleted"}, status=status.HTTP_204_NO_CONTENT)

