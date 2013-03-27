import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'crawlera.settings'
sys.path.append('/etc/crawlera-site')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
