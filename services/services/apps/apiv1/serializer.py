from rest_framework import serializers

from services.apps.service.models import Service


class ServiceModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Service
		exclude = ('id', )