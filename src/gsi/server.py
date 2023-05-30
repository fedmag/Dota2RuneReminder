""" dota2gsi.py """
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import queue
from json import loads as json_loads
import threading
import logging

log = logging.getLogger(__name__)


class CustomServer(ThreadingHTTPServer):

    def init_state(self, event_queue):
        self.q: queue.Queue = event_queue


class CustomRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        """ Receive state from GSI """
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')
        state = json_loads(body)
        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()
        self.server.q.put_nowait(state)  # type: ignore

    def log_message(self, format, *args):
        """ Don't print status messages """
        return


class ServerManager():

    def __init__(self, q: queue.Queue, ip='0.0.0.0', port=3000) -> None:
        super().__init__()
        self.ip = ip
        self.port = port
        self.q = q
        self.server = CustomServer((ip, port), CustomRequestHandler)

    def run(self):
        self.server.init_state(self.q)
        log.info(f"DotA 2 GSI server listening on {self.ip}:{self.port}")
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def stop(self):
        log.info("Stop signal received..")
        log.info("..shutting down server..")
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        log.info("..server stopped!")
