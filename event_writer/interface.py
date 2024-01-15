#!/usr/bin/env python3

from typing import Any

from types_ import Event


class iEventWriter:
    def __init__(self, target: Any) -> None:
        pass

    def write(self, event: Event) -> None:
        raise NotImplementedError()
