from rest_framework import serializers

from services.apps.service.models import Service


class ServiceModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Service
		exclude = ('id', )


class ServiceUpdateModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Service
		fields = ('status', )

	def update(self, instance, validated_data):

		instance.status = 'changed'
		instance.save()

		return instance


class ServiceRetriveModelSerializer(serializers.ModelSerializer):

	count = serializers.IntegerField(read_only=True)

	class Meta:
		model = Service
		fields = ('service_name', 'version', 'count')

