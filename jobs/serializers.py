from rest_framework import serializers
from .models import User, Job, JobCategory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class JobSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all(), source='category', write_only=True)
    category = serializers.StringRelatedField()
    posted_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        read_only = ['posted_at']

class CataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'