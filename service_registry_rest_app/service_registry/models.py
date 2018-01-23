# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# This stores services
class Service(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=6, default='0.0.1')
