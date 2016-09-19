from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from auth_remote import views
from django.contrib import admin
admin.autodiscover()
admin.site.login = views.adminlogin

urlpatterns = [
    url(r'^$', 'app.views.home', name='home'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),

    url(r'^login/', include('auth_remote.urls')),

    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
