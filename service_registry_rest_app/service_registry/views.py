# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from rest_framework import viewsets
# from serializers import ServiceSerializer
# from models import Service
# from django_filters.rest_framework import DjangoFilterBackend
#
# from rest_framework.response import Response
# from rest_framework import generics


# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from service_registry.models import Service
from service_registry.serializers import ServiceSerializer
from django.db.models import Count
import json

@csrf_exempt
def snippet_list(request):
    """
    List all code service, or create a new service.
    """
    if request.method == 'GET':
        name = request.GET.get('name', None)
        version = request.GET.get('version', None)
        queryset = Service.objects.all()

        if name is not None:
            queryset = queryset.filter(name=name)

        if version is not None:
            queryset = queryset.filter(version=version)

        services = queryset.values('name', 'version').annotate(count=Count('version'))
        serializer = ServiceSerializer(services, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.body
        data = json.loads(data)
        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServiceSerializer(service, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        service.delete()
        return HttpResponse(status=204)