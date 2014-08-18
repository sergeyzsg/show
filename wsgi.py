from __future__ import unicode_literals

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

os.chdir(PROJECT_ROOT)
sys.path.insert(0, PROJECT_ROOT)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
