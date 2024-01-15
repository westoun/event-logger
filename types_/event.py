#!/usr/bin/env python3

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    event_type: str
    timestamp: datetime
    user_id: str = None
    payload: str = None
