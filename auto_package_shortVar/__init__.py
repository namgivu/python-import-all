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
    mdl = importlib.import_module(modulePath)

    #make referenced variables shorten ref. https://stackoverflow.com/questions/14071135/import-file-using-string-as-name/14071252?noredirect=1#comment75519547_14071252
    globals().update(mdl.__dict__)


pass
#Above code can be made tiny in auto_app_tiny.py