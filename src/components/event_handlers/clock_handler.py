# def clock_handler(last_state, state):
#     if states_are_usable(last_state, state):
#         new_clock = state.get("map").get("clock_time")
#         last_clock = last_state.get("map").get("clock_time")
#         if last_clock != new_clock:
#             return new_clock
#     return None

# def states_are_usable(last_state, state):
#     return last_state is not None and state is not None and state.get("map") is not None and last_state.get("map") is not None

from typing import Any
from .event_handler import EventHandlerInterface
import logging

log = logging.getLogger(__name__)

class ClockEventHandler(EventHandlerInterface):
    
    def __init__(self) -> None:
        super().__init__()
        self.last_state: Any = None
        self.handler_name : str = "Clock handler"
        self.game_clock: int = 0
        
    def handle_event(self, event) -> None:
        if self.states_are_usable(event):
            new_clock = event.get("map").get("clock_time")
            last_clock = self.last_state.get("map").get("clock_time")
            if last_clock != new_clock:
                log.info(new_clock)
                self.last_state = event
                self.game_clock = new_clock
        self.last_state = event
        
    def get_game_clock(self) -> int:
        return self.game_clock
    
    def states_are_usable(self, state):
        return self.last_state is not None and state is not None and state.get("map") is not None and self.last_state.get("map") is not None
    
    def get_handler_name(self):
        return self.handler_name