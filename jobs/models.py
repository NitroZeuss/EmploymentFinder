from django.db import models
from EmploymentFinder.settings import AUTH_USER_MODEL

# Create your models here.

## User Model 
class User(models.Model):
    User = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    stats = models.CharField(max_length=1000)
    gmail = models.CharField(max_length=100)

# Other 
    
class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
