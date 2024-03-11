from django.contrib import admin
from django.urls import path
from .import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', views.UsersViewset)
router.register('Jobs', views.JobViewSet)
router.urls

urlpatterns = router.urls


# urlpatterns = [
#     path("users/", views.Users),
#     path("Jobs/", views.Jobs),
#     path('category/', views.job_category_view)
# ]
