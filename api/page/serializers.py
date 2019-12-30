from rest_framework import serializers
from .models import NP

class NPSerializer(serializers.ModelSerializer):
    class Meta:
        model = NP
        fields = "__all__"