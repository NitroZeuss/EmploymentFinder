from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User, Job, JobCategory
from .serializers import UserSerializer, JobSerializer, CataSerializer


# Create your views here.

class UsersViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Product View logic
class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


@api_view(['GET'])
def job_category_view(request):  # Rename the view function
    queryset = JobCategory.objects.all()
    serializer = CataSerializer(queryset, many=True)
    return Response(serializer.data)
