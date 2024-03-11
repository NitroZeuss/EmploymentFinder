from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.JobCategory)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Application)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass