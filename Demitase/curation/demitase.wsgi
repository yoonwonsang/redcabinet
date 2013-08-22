import os
import sys

path = '/home/fivestar/Fivestar/redcabinet/Demitase/curation'
if path not in sys.path:
    sys.path.insert(0, '/home/fivestar/Fivestar/redcabinet/Demitase/curation')

os.environ['DJANGO_SETTINGS_MODULE'] = 'curation.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

