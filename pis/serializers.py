from rest_framework import serializers
from .models import Pi


class PiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pi
        fields = '__all__'