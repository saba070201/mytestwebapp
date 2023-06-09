import os
import sys

# assuming your django settings file is at '/home/denniskot/mysite/mysite/settings.py'
# and your manage.py is is at '/home/denniskot/mysite/manage.py'
path = '/home/saba07022001/myapp/testwebapp/src/newssite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'newssite.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()