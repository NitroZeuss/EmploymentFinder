from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("users/", views.Users),
    path("Jobs/", views.Jobs),
    path('category/', views.job_category_view)
]
