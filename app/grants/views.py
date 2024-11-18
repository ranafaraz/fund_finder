from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Grant
from .serializers import GrantSerializer

class GrantViewSet(ModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer

    def list(self, request, *args, **kwargs):
        """
        Override list to return grants as a flat JSON array.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)  # Flat array of grants
