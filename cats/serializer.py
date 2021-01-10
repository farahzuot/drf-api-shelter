from rest_framework import serializers

from .models import Cats_data

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name', 'status', 'owner')
        model = Cats_data