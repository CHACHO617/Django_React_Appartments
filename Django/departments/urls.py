from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet

# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)

# Include the router-generated URL patterns
urlpatterns = router.urls
