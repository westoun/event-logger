#!/usr/bin/env python3

from typing import Any

from types_ import Event
from .interface import iEventWriter


class TextWriter(iEventWriter):
    def __init__(self, target: Any) -> None:
        self._target_path = target

    def write(self, event: Event) -> None:
        event_string = f"{event.timestamp.isoformat()} type: {event.event_type}"

        if event.user_id is not None:
            event_string += f" user: {event.user_id}"

        if event.payload is not None:
            event_string += f" payload: '{event.payload}'"

        with open(self._target_path, "a") as target_file:
            target_file.write(event_string)
            target_file.write("\n")
