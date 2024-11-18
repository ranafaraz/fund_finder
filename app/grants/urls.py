from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrantViewSet

# Create a router and register the GrantViewSet
router = DefaultRouter()
router.register(r'grants', GrantViewSet, basename='grant')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
