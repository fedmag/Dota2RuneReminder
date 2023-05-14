""" dota2gsi.py """
from collections.abc import Callable, Iterable, Mapping
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import queue
from json import loads as json_loads
from typing import Any
from .handlers import clock_handler
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
            # print(f"Calling handler {handler.__name__}")
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
        handler_response = self.server.handle_state(state) # type: ignore
        if handler_response is not None:
            self.server.q.put_nowait(handler_response) # type: ignore
        self.server.last_state = state  # type: ignore

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
        self.add_handlers_to_server([clock_handler])
        log.info(f"DotA 2 GSI server listening on {self.ip}:{self.port} - CTRL+C to stop")
        if len(self.server.handlers) == 0:
            print("Warning: no handlers were added, nothing will happen")
        try:
            self.server.serve_forever()
        except (KeyboardInterrupt, SystemExit):
            pass
        # self.server.server_close()

    def on_update(self, func):
        """ Sets the function to be called when a new state is available.
        
        The function must accept two arguments:
            last_state - the previous state
            state - the new state
        """
        self.server.handlers.append(func)

    def add_handlers_to_server(self, handlers: list):
        for handler in handlers:
            self.on_update(handler)
            
    def join(self, timeout: float | None = None) -> None:
        log.info("Join signal received")
        return super().join(timeout)
    
    
    def stop(self):
        log.info("Stop signal received..")
        log.info("..shutting down server..")
        self.server.shutdown()
        log.info("..server stopped!")

