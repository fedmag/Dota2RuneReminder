from typing import Any
from .event_handler import EventHandlerInterface
import logging

log = logging.getLogger(__name__)

class ClockEventHandler(EventHandlerInterface):
    """ Handler that exposes the game clock.
    Once the state is passed to this handler through handle_state(state), the in game clock can be retrieved using 
    get_game_clock().
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.last_state: Any = None
        self.handler_name : str = "Clock handler"
        self.game_clock: int = -9999
        
    def handle_state(self, state) -> None:
        if self.states_are_usable(state):
            new_clock = state.get("map").get("clock_time")
            last_clock = self.last_state.get("map").get("clock_time")
            if last_clock != new_clock:
                log.info(new_clock)
                self.last_state = state
                self.game_clock = new_clock
        self.last_state = state
        
    def get_game_clock(self) -> int:
        return self.game_clock
    
    def states_are_usable(self, state):
        return self.last_state is not None and state is not None and state.get("map") is not None and self.last_state.get("map") is not None
    
    def get_handler_name(self):
        return self.handler_name