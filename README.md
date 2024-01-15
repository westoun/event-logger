# Event Logger Server

This repository contains a minimalistic logging server, that expects
event information from a frontend application and writes it to a
text-file, csv-file, or stout.

## Installation

Before you are able to run the server, make sure you have all required
dependencies installed. Locally, I recommend installing through a virtual
environment as follows:

Create a virtual environment:

```bash
python3 -m venv venv
```

To activate the virtual environment, execute:

```bash
source venv/bin/activate
```

Then, install all python libraries, the project relies on using
the package manager [pip](https://pip.pypa.io/en/stable/):

```bash
pip3 install -r requirements.txt
```

If you are running it via docker, simply
build from the Dockerfile.

## Usage

To start the server, run

```bash
uvicorn server:app -p 8000
```

Depending on your setup, you might have to use
a different port.
If the frontend is running on a different url, you
might also have to include fastapi's CORS-middleware
in server.py.

For testing purposes, the /test-route serves a simple
HTML page firing text and click events to the server.
