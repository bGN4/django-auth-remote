from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()
admin.site.login_template='remotelogin1.html'

urlpatterns = [
    url(r'^$', 'app.views.home', name='home'),
    url(r'^login/$', 'auth_remote.views.remotelogin', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),

    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
