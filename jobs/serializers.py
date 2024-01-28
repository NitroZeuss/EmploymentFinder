from rest_framework import serializers
from .models import User , Job, JobCategory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'User', 'gmail']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__' 
        #fields  = ['id', 'title', 'company', 'posted_by', 'posted_at']

class CtatSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'