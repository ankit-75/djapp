"""
WSGI config for djapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#from dj_static import Cling
#from whitenoise.django import DjangoWhiteNoise
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ankit-djapp.settings')

#application = get_wsgi_application()
#application = Cling(get_wsgi_application())
#application = DjangoWhiteNoise(application)

if settings.DEBUG:
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = get_wsgi_application()
    