from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User , Job, JobCategory
from .serializers import UserSerializer, JobSerializer, CtatSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def Users(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(request.data)
        if serializer.is_valid:
            serializer.save
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def Jobs(request):
    if request.method == 'GET':
        queryset = Job.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def job_category_view(request):  # Rename the view function
    queryset = JobCategory.objects.all()
    serializer = CtatSerializer(queryset, many=True)
    return Response(serializer.data)

