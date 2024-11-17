from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrantViewSet

router = DefaultRouter()
router.register(r'', GrantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
