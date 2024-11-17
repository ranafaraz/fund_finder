from rest_framework.viewsets import ModelViewSet
from .models import Grant
from .serializers import GrantSerializer

class GrantViewSet(ModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer
