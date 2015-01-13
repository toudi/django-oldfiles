# django-oldfiles
handy utility for removing old NamedTemporaryFile

this django app is supposed to be used whenever you have to create a NamedTemporaryFile(delete=False) and want to limit how long should it be on the disk.

# Usage

1. add 'oldfiles' into `INSTALLED_APPS`
2. issue a command: manage.py remove_old_files

## Available settings
(To be put in your `settings.py`).
You can use those settings to nicely bound with NamedTemporaryFile, like so:
```
from tempfile import NamedTemporaryFile
from oldfiles import settings as ofs
myfile = NamedTemporaryFile(delete=False, dir=ofs.OLDFILES_DIR)
```
the reason behind importing the oldfiles settings module rather than django settings is that oldfiles's one will always have the non-null value. It is completely ok to pass None as `dir` parameter to NamedTemporaryFile constructor, but it is not ok to pass empty string to find command.
### OLDFILES_DIR
the path which holds the files (defaults to /tmp)
### OLDFILES_DELTA
how old must be the files to be got rid of (defaults to 1 hour)
### OLDFILES_METHOD
how should be the files removed; possible values:
* `find` - use find command (should be faster)
* `naive` - use naive implementation (uses os.listdir under the hood)
