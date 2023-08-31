import importlib
import pkgutil


def import_submodules(package_name):
    package = importlib.import_module(package_name)
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package_name}.{name}")
