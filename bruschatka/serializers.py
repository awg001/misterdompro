from rest_framework import serializers
from .models import Bruschatka


class BruschatkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bruschatka

        fields = '__all__'
