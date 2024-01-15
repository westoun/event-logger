#!/usr/bin/env python3

from os import path
from typing import Any

from types_ import Event
from .interface import iEventWriter


class CsvWriter(iEventWriter):
    def __init__(self, target: Any) -> None:
        self._target_path = target

    def write(self, event: Event) -> None:
        if not path.isfile(self._target_path):
            with open(self._target_path, "w") as target_file:
                target_file.write("timestamp;event_type;user_id;payload\n")

        with open(self._target_path, "a") as target_file:
            target_file.write(
                f"{event.timestamp};{event.event_type};{event.user_id};{event.payload}\n"
            )
