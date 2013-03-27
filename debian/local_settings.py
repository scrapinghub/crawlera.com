# This file is deployed by APT and not recommended to be modified manually.
# Instead, add a /etc/crawlera-site/server_settings.py file for your custom
# settings.

import socket

DEBUG = False

MAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[crawlera-site] '
SERVER_EMAIL = 'crawlera-site@%s' % socket.getfqdn()
ADMINS = [('Errors', 'errors@scrapinghub.com')]

# crawlera-site doesn't require a database (yet)
#DATABASE_ENGINE = 'sqlite3'
#DATABASE_NAME = '/var/lib/crawlera-site/crawlera-site.db'
#DATABASE_USER = ''
#DATABASE_PASSWORD = ''

TEMPLATE_DIRS = ['/usr/share/crawlera-site/templates']
MEDIA_ROOT = '/usr/share/crawlera-site/static'

try:
    from server_settings import *
except ImportError:
    pass
