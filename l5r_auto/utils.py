import importlib
import logging
import pkgutil


def import_submodules(package_name):
    logging.debug("Importing submodules for %s", package_name)
    package = importlib.import_module(package_name)
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__):
        if is_pkg:
            import_submodules(f"{package_name}.{name}")
        else:
            importlib.import_module(f"{package_name}.{name}")
