from django.core.management.base import NoArgsCommand
from oldfiles import settings
from datetime import datetime
import time
from subprocess import call
import os
# uses code from http://stackoverflow.com/questions/12329367/limiting-the-lifetime-of-a-file-in-python


class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        if settings.OLDFILES_METHOD == 'find':
            self.handle_find()
        else:
            self.handle_naive()

    def handle_find(self):
        minutes = int(settings.OLDFILES_DELTA.total_seconds() / 60)
        call((
            'find',
            settings.OLDFILES_DIR,
            '-type',
            'f',
            '-mmin',
            '+%d' % minutes,
            '-delete'
        ))

    def handle_naive(self):
        delta = settings.OLDFILES_DELTA.total_seconds()
        _now = time.mktime(datetime.now().timetuple())
        for _f in os.listdir(settings.OLDFILES_DIR):
            if os.path.isfile(_f):
                _f_time = os.path.getmtime(_f)
                if _now - _f_time < delta:
                    try:
                        os.unlink(_f)
                    except IOError:
                        pass
