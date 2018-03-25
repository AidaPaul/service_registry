# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Count

from rest_framework import generics, status
from rest_framework.response import Response

from .serializer import ServiceModelSerializer, ServiceUpdateModelSerializer, ServiceRetriveModelSerializer
from services.apps.service.models import Service


class ServiceCreateView(generics.CreateAPIView):

	serializer_class = ServiceModelSerializer


class ServiceUpdateView(generics.UpdateAPIView):

	serializer_class = ServiceUpdateModelSerializer
	queryset = Service.objects.all()



class ServiceDeleteView(generics.DestroyAPIView):

	serializer_class = ServiceModelSerializer
	queryset = Service.objects.all()


	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		return Response({'service': instance.service, 'change': 'removed'})


class ServiceRetriveView(generics.RetrieveAPIView):

	serializer_class = ServiceRetriveModelSerializer
	queryset = Service.objects.all()

	def get_object(self):
		
		service = self.request.query_params.get('service')
		version = self.request.query_params.get('version')

		if service and version:
			qs = self.queryset.filter(service=service, version=version).values('service', 'version').annotate(count=Count('service'))
		elif not version:
			qs = self.queryset.filter(service=service).values('service', 'version').annotate(count=Count('service'))

		if qs:
			return qs[0]


	def get(self, request, *args, **kwargs):

		service = self.request.query_params.get('service')
		version = self.request.query_params.get('version')

		if not service and not version:
			return Response({}, status.HTTP_400_BAD_REQUEST)
		if not service:
			return Response({}, status.HTTP_400_BAD_REQUEST)


		instance = self.get_object()

		if instance:
			serializer = self.serializer_class(instance, context={'request': request}, many=False)
			response_dict = serializer.data
			if not version:
				response_dict.pop('version')
			return Response(response_dict, status.HTTP_200_OK)
		return Response({'service':service, 'version':version, 'count':0}, status.HTTP_404_NOT_FOUND)


					
