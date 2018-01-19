# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from serializers import ServiceSerializer
from models import Service
from django_filters.rest_framework import DjangoFilterBackend


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Services to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'version')
