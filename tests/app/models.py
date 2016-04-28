#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Musician(models.Model):
    name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

