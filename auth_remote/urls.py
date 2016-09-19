from django.conf.urls import url, include
from .views import remotelogin
from . import __appname__ as appname

url_list = [
    url(r'^$', remotelogin, name='login')
]

urlpatterns = [
    url(r'^$', include(url_list,appname,appname))
]
