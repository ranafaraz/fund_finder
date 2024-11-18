from rest_framework import serializers
from .models import Grant

class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = "__all__"  # Include all fields from the Grant model
