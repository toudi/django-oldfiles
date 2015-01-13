from django.conf import settings
from datetime import timedelta

OLDFILES_DIR = getattr(settings, 'OLDFILES_DIR', '/tmp')
OLDFILES_DELTA = getattr(settings, 'OLDFILES_DELTA', timedelta(hours=1))
OLDFILES_METHOD = getattr(settings, 'OLDFILES_METHOD', 'find')
