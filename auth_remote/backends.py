from __future__ import unicode_literals

from django.utils.six.moves.urllib.parse import urlparse, urlunparse, urlencode, parse_qsl
from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import get_user_model
import datetime
import logging
import urllib2
import time
import json

logger = logging.getLogger('django.auth.backends')

def no_check_cert():
    try:
        import ssl
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx
    except:
        return None

class RemoteAuthBackend(RemoteUserBackend):

    def authenticate(self, username=None, password=None, token=None):
        user = None
        try: token = token or dict(parse_qsl(password.lstrip('? '))).get('sid')
        except: pass
        if not token: return user
        data = None
        try: data = json.loads( urllib2.urlopen("%s?sid=%s"%(settings.LOGIN_URL, token), timeout=8, context=no_check_cert()).read() )
        except: data = None
        if data is not None and data.has_key('user'):
            UserModel = get_user_model()
            if self.create_unknown_user:
                user, created = UserModel._default_manager.get_or_create(defaults={
                                    'email'      : data.get('mail', ''),
                                    'first_name' : data.get('display', ''),
                                    'is_staff'   : True,
                                    'last_login' : datetime.datetime.now(),
                                    #'member_of' : data.get('memberOf', ''),
                                }, **{
                                    UserModel.USERNAME_FIELD: data['user'],
                                })
                if created:
                    user = self.configure_user(user)
            else:
                try:
                    user = UserModel._default_manager.get_by_natural_key(data['username'])
                except UserModel.DoesNotExist:
                    pass
        logger.debug( 'authenticate user {0}'.format(user) )
        return user

    def clean_username(self, username):
        return username

    def configure_user(self, user):
        return user
