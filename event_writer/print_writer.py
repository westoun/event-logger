#!/usr/bin/env python3

from typing import Any

from types_ import Event
from .interface import iEventWriter


class PrintWriter(iEventWriter):
    def __init__(self, target: Any = None) -> None:
        pass

    def write(self, event: Event) -> None:
        event_string = f"{event.timestamp.isoformat()} type: {event.event_type}"

        if event.user_id is not None:
            event_string += f" user: {event.user_id}"

        if event.payload is not None:
            event_string += f" payload: '{event.payload}'"

        print(event_string)
