#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from models import *
import traceback
import logging


def home(request):
    return HttpResponse('home')


