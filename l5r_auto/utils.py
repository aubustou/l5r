from __future__ import annotations

import importlib
import logging
import pkgutil
from dataclasses import dataclass
from typing import TYPE_CHECKING, Type, TypeGuard, TypeVar, dataclass_transform

if TYPE_CHECKING:
    from .cards import Entity


def import_submodules(package_name):
    logging.debug("Importing submodules for %s", package_name)
    package = importlib.import_module(package_name)
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__):
        if is_pkg:
            import_submodules(f"{package_name}.{name}")
        else:
            importlib.import_module(f"{package_name}.{name}")


T = TypeVar("T")


def is_entity_of_type(entity: Entity, entity_type: Type[T]) -> TypeGuard[T]:
    return isinstance(entity, entity_type)


dataclass_ = dataclass_transform()(dataclass(repr=False, kw_only=True))
