from __future__ import annotations
from typing import Callable

from l5r_auto.errors import WrongStateError


def pay_cost(actions: Callable[[], None] | list[Callable[[], None]]) -> bool:
    if not isinstance(actions, list):
        actions = [actions]

    for action in actions:
        try:
            action()
        except WrongStateError:
            return False

    return True
