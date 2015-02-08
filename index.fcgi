#!/home4/fareed83/pyenv27/bin/python
##!/usr/bin/python

import sys, os
import site

# Add a custom Python path. (optional)
sys.path.insert(0, "/home/fareed83/pyen27v/lib/python2.7/site-packages/")
site.addsitedir('/home/fareed83/public_html/triplea.in/ola/app')
file('mysyspath.txt', 'w').write(repr(sys.path))

# Switch to the directory of your project
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ.setdefault('LANG', 'en_US.UTF-8')

#os.environ['PATH'] = '/home4/fareed83/pyenv/bin:' + os.environ['PATH']
#os.environ['VIRTUAL_ENV'] = '/home4/fareed83/pyenv'

#os.chdir("/home/fareed83/public_html/api/webregistry/nowr/")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "app.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
