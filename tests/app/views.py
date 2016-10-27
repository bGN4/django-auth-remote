#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from models import *
import traceback
import logging


def home(request):
    return HttpResponse('home')


@login_required(login_url='/login/',redirect_field_name=settings.REDIRECT_FIELD_NAME)
def about(request):
    return HttpResponse('about')

