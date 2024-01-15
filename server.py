#!/usr/bin/env python3

from datetime import datetime
from fastapi import FastAPI, Response, Request, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from types_ import Event
from event_writer import iEventWriter, PrintWriter, TextWriter, CsvWriter

app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins="http://localhost:4200",
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

templates = Jinja2Templates(directory="templates")

writer: iEventWriter = CsvWriter(target="event_log.csv")
# writer: iEventWriter = TextWriter(target="event_log.txt")
# writer: iEventWriter = PrintWriter()


@app.get("/test")
def return_test_page(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})


@app.post("/log-event")
async def log_event(request: Request):
    body = await request.json()

    event_type = body["event_type"]

    timestamp = body["timestamp"]  # expected as iso 8601
    timestamp = datetime.fromisoformat(timestamp)

    if "user_id" in body:
        user_id = body["user_id"]
    else:
        user_id = None

    if "payload" in body:
        payload = body["payload"]
    else:
        payload = None

    event: Event = Event(
        event_type=event_type, user_id=user_id, timestamp=timestamp, payload=payload
    )
    writer.write(event)
