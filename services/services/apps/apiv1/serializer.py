from rest_framework import serializers

from services.apps.service.models import Service


class ServiceModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Service
		exclude = ('id', )


class ServiceUpdateModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Service
		fields = ('change', )

	def update(self, instance, validated_data):

		instance.change = 'changed'
		instance.save()

		return instance


class ServiceRetriveModelSerializer(serializers.ModelSerializer):

	count = serializers.IntegerField(read_only=True)


	def __init__(self, *args, **kwargs):

		super(ServiceRetriveModelSerializer, self).__init__(*args, **kwargs)

		# remove 'version' field not exists
		service = self.context['request'].query_params.get('service', None)
		version = self.context['request'].query_params.get('version', None)

		# remove version from fields
		if version is None:
			self.fields.pop('version')


	class Meta:
		model = Service
		fields = ('service', 'version', 'count')

