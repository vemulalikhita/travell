"""
WSGI config for travell project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

path = '\Users\Vemula Likhita\travell\travell\settings.py'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travell.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
