from components.event import Event
import time
import logging

log = logging.getLogger(__name__)

class CountDown:

    def __init__(self, event: Event) -> None:
        log.info(f"Setting up timer for {event.name}")
        self.__event = event
        self.__OFFSET = 15
        self.__last_played: int = 0
    
    def get_event_name(self):
        return self.__event.name
    
    def handle_time(self, game_clock: int) -> bool:
        if game_clock < 1 or (not self.__event.recurring and self.__last_played != 0): return False # for single time events (like tormentor)
        if (game_clock + self.__OFFSET) % self.__event.amount == 0 and game_clock != self.__last_played:
            self.__last_played = game_clock
            return True
        return False