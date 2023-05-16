""" dota2gsi.py """
from collections.abc import Callable, Iterable, Mapping
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import queue
from json import loads as json_loads
from typing import Any
import threading
import logging

log = logging.getLogger(__name__)

class CustomServer(ThreadingHTTPServer):
    
    def init_state(self, event_queue):
        self.last_state: str | None = None
        self.handlers = []
        self.q : queue.Queue = event_queue

    def handle_state(self, state):
        for handler in self.handlers:
            return handler(self.last_state, state)


class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        """ Receive state from GSI """
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')
        state = json_loads(body)
        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()
        self.server.q.put_nowait(state) # type: ignore

    def log_message(self, format, *args):
        """ Don't print status messages """
        return

class ServerManager(threading.Thread):
    
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None, ip='0.0.0.0', port=3000, q: queue.Queue) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.ip = ip
        self.port = port
        self.q = q
        self.server = CustomServer((ip, port), CustomRequestHandler)


    def run(self):
        self.server.init_state(self.q)
        # self.add_handlers_to_server([clock_handler])
        log.info(f"DotA 2 GSI server listening on {self.ip}:{self.port} - CTRL+C to stop")
        self.server.serve_forever()

    def stop(self):
        log.info("Stop signal received..")
        log.info("..shutting down server..")
        self.server.shutdown()
        log.info("..server stopped!")

