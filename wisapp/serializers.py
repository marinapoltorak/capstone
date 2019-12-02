from rest_framework import serializers

from .models import Scientist

class ScientistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scientist
        fields = '__all__'
