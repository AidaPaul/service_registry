from models import Service
from rest_framework import serializers



class ServiceSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    version = serializers.CharField(required=False, allow_blank=True, max_length=6)
    count = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.version = validated_data.get('version', instance.version)
        instance.save()
        return instance




