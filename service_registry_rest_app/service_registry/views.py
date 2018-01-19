# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from serializers import ServiceSerializer
from models import Service
from rest_framework import filters


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Services to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)
