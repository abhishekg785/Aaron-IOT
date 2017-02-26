import os
import pkgutil

path = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
print path
location = [path]
for finder, name, ispkg in pkgutil.walk_packages(location):
	try:
		loader = finder.find_module(name)
		mod = loader.load_module(name)
	except:
		print 'error'
