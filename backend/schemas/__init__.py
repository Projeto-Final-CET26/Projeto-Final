from importlib import import_module
from inspect import isclass
from pkgutil import iter_modules

from pydantic import BaseModel

__all__: list[str] = []

for module_info in sorted(iter_modules(__path__), key=lambda module: module.name):
    module = import_module(f".{module_info.name}", __name__)
    for name, value in vars(module).items():
        if isclass(value) and issubclass(value, BaseModel) and value is not BaseModel:
            globals()[name] = value
            __all__.append(name)
