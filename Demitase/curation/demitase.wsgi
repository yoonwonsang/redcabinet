import os
import sys

path = '/home/fivestar/Fivestar/demitase/Demitase/curation'
if path not in sys.path:
    sys.path.insert(0, '/home/fivestar/Fivestar/demitase/Demitase/curation')

os.environ['DJANGO_SETTINGS_MODULE'] = 'curation.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

