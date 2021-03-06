##region auto-import the module files in this package folder
packagePath='auto_package_shortVar'

"""list to import ref. https://stackoverflow.com/a/1057534/248616"""

#list all modules ie. *.py files
from os.path import dirname, basename, isfile
import glob
fileALL = glob.glob(dirname(__file__) + "/*.py")

#import those modules
"""import from string value ref. https://stackoverflow.com/a/8719100/248616"""
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

"""
NOTE about reference to variables/methods defined in other package 
- If reference declared IN sub-modules in this package, they only visible WITHIN that sub-module   
- If reference declared HERE ie. __init__.py file, they are VISIBLE to outer code when they call 'from $THIS_MODULE import *'   
"""