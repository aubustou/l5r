from dataclasses import dataclass as dataclass_, field


def dataclass(*args, **kwargs):
    kwargs["kw_only"] = True
    return dataclass_(*args, **kwargs)
