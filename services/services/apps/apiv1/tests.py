# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from services.apps.service.models import Service


class ServiceMixin(object):

    def setUp(self):
        self.s1 = Service.objects.create(service='postgres', version='9.6')
        self.s2 = Service.objects.create(service='mysql', version='5.2')
        self.s3 = Service.objects.create(service='celery', version='1.0')
        self.s4 = Service.objects.create(service='fail2ban', version='4.6')
        self.s5 = Service.objects.create(service='postgres', version='9.6')


class ServiceAPITestCases(ServiceMixin, APITestCase):

    def test_create_service(self):
        

        """
            POST /apiv1/create/ must return status code 201 and response
            {'service': 'apache', 'version': '0.0.1', 'change': 'created'}
        """

        response = self.client.post(reverse('apiv1:create'), {'service': 'apache', 'version': '0.0.1'})
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        self.assertJSONEqual(response.content, {'service': 'apache', 'version': '0.0.1', 'change': 'created'})

    def test_find_service(self):
        """
            GET /apiv1/search/ must return status code 200 and
            response {'service': 'postgres', 'version': '9.6', 'count':2}
        """

        response = self.client.get(reverse('apiv1:search'), {'service': 'postgres', 'version': '9.6'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertJSONEqual(response.content, {'service': 'postgres', 'version': '9.6', 'count':2})

    def test_find_non_existing_service(self):
        """
            GET /api/v1/search/ must return status code 404 and
            response {'service': 'sample', 'version': '1.1.4', 'count':0}
        """

        response = self.client.get(reverse('apiv1:search'), {'service': 'sample', 'version': '1.1.4'})
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

        self.assertJSONEqual(response.content, {'service': 'sample', 'version': '1.1.4', 'count': 0})

    def test_find_service_without_version(self):
        """
            GET /apiv1/search/ must return status code 200 and
            response {'service': 'postgres', 'count': 2}
        """

        response = self.client.get(reverse('apiv1:search'), {'service': 'postgres'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertJSONEqual(response.content, {'service': 'postgres', 'count': 2})

    def test_search_missing_parameter(self):
        """GET /apiv1/search/ must return status code 400"""

        response = self.client.get(reverse('apiv1:search'), {'version': '0.0.1'})
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)


    def test_update_service(self):
        """
            PUT /apiv1/search/ must return status code 200 and
            response {'change': 'changed'}
        """

        response = self.client.put(reverse('apiv1:update', args=[self.s3.pk]), {'service': 'celery-mq', 'version': '1.4.5'},
                               )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertJSONEqual(response.content, {'change': 'changed'})

    def test_remove_service(self):
        """
            DELETE /apiv1/delete/ must return status code 200 and
            response {'service': 'fail2ban', 'change': 'removed'}
        """

        response = self.client.delete(reverse('apiv1:delete', args=[self.s4.pk]),
                                  )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertJSONEqual(response.content, {'service': self.s4.service, 'change': 'removed'})