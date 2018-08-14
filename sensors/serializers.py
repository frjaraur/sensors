from rest_framework import serializers
from sensors.models import Sensor


class SensorsSerializer(serializers.Serializer):

    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    ip = models.CharField(max_length=15,default='0.0.0.0')
    enabled = models.BooleanField(default=False)
    update = models.DateTimeField(auto_now=False, auto_now_add=False)
    humidity = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    """
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField()
    name = serializers.CharField(max_length=255)
    #description = serializers.TextField()
    location = serializers.CharField(max_length=255)
    ip = serializers.CharField(max_length=15,default='0.0.0.0')
    enabled = serializers.BooleanField(default=False)
    #update = serializers.DateTimeField(auto_now=False, auto_now_add=False)
    humidity = serializers.IntegerField(default=0)
    temperature = serializers.IntegerField(default=0)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.ip = validated_data.get('ip', instance.ip)
        instance.enabled = validated_data.get('enabled', instance.enabled)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.save()
        return instance
