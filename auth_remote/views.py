#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.views import login
from django.contrib.auth import REDIRECT_FIELD_NAME
#from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django import http

#@csrf_protect
def remotelogin(request):
    if request.method in ('GET',) and 'sid' not in request.GET:
        return http.HttpResponseRedirect('/admin/login')
    response = login(request, 
                 template_name='remotelogin2.html',
                 authentication_form=AdminAuthenticationForm,
                 current_app='auth_remote',
                 extra_context={
                     'title'   : _('Log in'),
                     'app_path': request.path,
                     REDIRECT_FIELD_NAME: '/admin',
                 })
    errors = getattr(getattr(response, 'context_data', {}).get('form'), 'errors', {})
    if len(errors)>0:
        return http.HttpResponseRedirect('/admin/login')
    return response

