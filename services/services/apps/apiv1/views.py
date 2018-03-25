# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from .serializer import ServiceModelSerializer


class ServiceCreateView(generics.CreateAPIView):

	serializer_class = ServiceModelSerializer


	def post(self, request, *args, **kwargs):
		self.create(request, *args, **kwargs)
		return Response(status=status.HTTP_200_OK)



class ServiceUpdateView(generics.UpdateAPIView):

	serializer_class = ServiceModelSerializer


	def patch(self, request, *args, **kwargs):
		self.update(request, *args, **kwargs)



class ServiceDeleteView(generics.DestroyAPIView):

	serializer_class = ServiceModelSerializer


	def delete(self, request, *args, **kwargs):
		self.delete(request, *args, **kwargs)


class ServiceRetriveView(generics.RetrieveAPIView):

	serializer_class = ServiceModelSerializer

	def get(self, request, *args, **kwargs):
		self.retrive(request, *args, **kwargs)
