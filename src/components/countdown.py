from components.event import Event
import time

class CountDown:

    def __init__(self, event: Event) -> None:
        print(f"Setting up timer for {event.name}")
        self.__event = event
        self.start_timer()

    def start_timer(self):
        print(f"Starting timer for {self.__event.name}")
        self.__time = time.time()

    def should_sound_alarm(self) -> bool:
        if self.__time != None:
            self.elasped_time = time.time() - self.__time
            if self.elasped_time > self.__event.amount:
                print(f"Elasped time: {self.elasped_time} --- amount: {self.__event.amount}")
                self.start_timer()
                return True
        return False
    
    def get_event_name(self):
        return self.__event.name