# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Service(models.Model):


	""" Service Model """


	class STATUS(object):

		created = 'created'
		updated = 'updated'
		changed = 'changed'

	STATUS_CHOICES = (
		(STATUS.created, 'created'),
		(STATUS.updated, 'updated'),
		(STATUS.changed, 'changed')
	)

	service = models.CharField(max_length=30, help_text='service name')
	version = models.CharField(max_length=10, help_text='service version')
	change = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS.created)


	def __str__(self):
		return '{} - {}'.format(self.service, self.version)