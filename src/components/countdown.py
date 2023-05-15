from components.event import Event
import time
import logging

log = logging.getLogger(__name__)

class CountDown:

    def __init__(self, event: Event) -> None:
        log.info(f"Setting up timer for {event.name}")
        self.__event = event
        self.OFFSET = 15
    
    def get_event_name(self):
        return self.__event.name
    
    def handle_time(self, game_clock: int) -> bool:
        # log.debug(f"game with offset: {game_clock + self.OFFSET} - amount {self.__event.amount} -  modulo:  {(game_clock + self.OFFSET) % self.__event.amount} ")
        if (game_clock + self.OFFSET) % self.__event.amount == 0:
            return True
        return False