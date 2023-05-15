import logging
from .event_handler import EventHandlerInterface

log = logging.getLogger(__name__)

class HandlerManager:
    
    def __init__(self) -> None:
        self.handlers: list[EventHandlerInterface] = []
        
    def handle_event(self, event):
        for handler in self.handlers:
            handler.handle_event(event)
            
    def add_handler(self, handler: EventHandlerInterface):
        log.info(f"adding_handler {handler.get_handler_name()}")
        self.handlers.append(handler)
        
    def remove_handler(self, handler: EventHandlerInterface):
        self.handlers.remove(handler)