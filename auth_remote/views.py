#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.views import login, redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME
#from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django import http
from . import __appname__ as appname

#@csrf_protect
def remotelogin(request):
    if request.method in ('GET',) and 'sid' not in request.GET:
        return http.HttpResponseRedirect('/admin/login')
    response = login(request, 
                 template_name='remotelogin.html',
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

def adminlogin(request, extra_context=None):
    if request.method == 'GET' and request.user.is_active and request.user.is_staff:
        # Already logged-in, redirect to admin index
        from django.contrib import admin
        index_path = reverse('admin:index', current_app=admin.site.name)
        return http.HttpResponseRedirect(index_path)
    resolved_login_url = resolve_url(settings.LOGIN_URL)
    redirect_login_url = request.build_absolute_uri( reverse('{app_label}:login'.format(app_label=appname)) )
    return redirect_to_login(redirect_login_url, resolved_login_url, getattr(settings,'REDIRECT_FIELD_NAME',REDIRECT_FIELD_NAME))

