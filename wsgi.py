import sys
path = '/var/www/webroot/ROOT/flaskr'
if path not in sys.path:
    sys.path.append(path)
from flaskr.__init__ import app
application = app