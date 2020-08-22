import pkgutil

for _, module_name, _ in pkgutil.walk_packages(__path__):
    __import__('.'.join([__name__, module_name]))
    del module_name
