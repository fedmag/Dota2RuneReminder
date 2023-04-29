from event import Event
from threading import Thread
from time import sleep

class CountDown:

    def __init__(self, event: Event) -> None:
        self.event = event
        self.is_running = False

    def __start_timer(self):
        sleep_duration = self.event.amount
        self.is_running = True
        while sleep_duration > 0:
            print(f"you have {sleep_duration} seconds left for {self.event.name} event")
            sleep(1)
            sleep_duration -= 1
        print(f"{self.event.name} event completed")
        self.is_running = False

    def run_timer(self):
        timer_thread = Thread(target=self.__start_timer)

        timer_thread.start()