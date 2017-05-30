##region auto-import the module files in this package folder
packagePath='auto_package'

#list all modules ie. *.py files
from os.path import dirname, basename, isfile
import glob
fileALL = glob.glob(dirname(__file__) + "/*.py")

#import those modules
import importlib
for f in fileALL:
  if isfile(f) and not f.endswith('__init__.py'):
    moduleName = basename(f)[:-3]
    modulePath = '%s.%s' % (packagePath, moduleName)
    mdl = importlib.import_module(modulePath)

    ##region make referenced variables shorten

    """ref. https://stackoverflow.com/a/31306598/248616 ; shorten version but include every thing here https://stackoverflow.com/a/31306598/248616"""

    #determine a list of names to copy to the current name space
    names = getattr(mdl, '__all__', [n for n in dir(mdl) if not n.startswith('_')])

    #copy those names into the current name space
    g = globals()
    for name in names:
      g[name] = getattr(mdl, name)

    pass
    ##endregion make referenced variables shorten

pass
##endregion auto-import the module files in this package folder
