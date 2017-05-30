#list all modules ie. *.py files
from os.path import dirname, basename, isfile
import glob
fileALL = glob.glob(dirname(__file__) + "/*.py")

#import those modules
import importlib
for f in fileALL:
  if isfile(f) and not f.endswith('__init__.py'):
    moduleName = basename(f)[:-3]
    modulePath = 'auto_package.%s' % moduleName
    importlib.import_module(modulePath)

#Above code can be made tiny in auto_app_tiny.py