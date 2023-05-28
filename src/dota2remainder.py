from typing import Dict
from components.countdown import CountDown
from components.event import Event
from components.event_handlers.clock_handler import ClockEventHandler
from sounds.speaker import Speaker
from gsi.server import ServerManager

import pystray
from PIL import Image, ImageDraw
import queue
import toml
import logging
import threading

log = logging.getLogger(__name__)

class Dota2RuneRemainder:
    
    def __init__(self, config: Dict) -> None:
        self.__running = False
        self.__stop_event = threading.Event()
        self.config: Dict = config
        self.q = queue.Queue()
        
    def is_running(self):
        return self.__running
    
    def change_running_state(self, run: bool):
        self.__running = run
        log.info(f"Running state changed to: {run}")
        if self.__running: # if running set event to false 
            self.__stop_event.clear()
            t = threading.Thread(target=self.run)
            t.start()
        else: 
            self.__stop_event.set() 
            self.stop()
    
    def stop(self):
        log.info("Starting shutdown procedure..")
        log.info("Interruption signal sent.")
        self.server.stop()
        self.speaker.stop()
        log.info("Resetting queue..")
        self.q = queue.Queue()
        log.info("Program stopped")
        
    def setup(self):
        self.q = queue.Queue()
        self.tracked_events = []
        
        events = self.config.get("events")
        if events is not None:
            for event in events:
                self.tracked_events.append(CountDown(Event.create_from_dict(**event)))

        self.server = ServerManager(q = self.q)
        self.server.run()

        self.clock_handler = ClockEventHandler()
        self.handlers = [
            self.clock_handler
        ]

        self.speaker = Speaker()
        self.speaker.say("Counters are set!")
        
    def run(self, ):  
        self.setup()      
        while True:
            if not self.__stop_event.is_set(): 
                try:
                    state: str = self.q.get(block=False)
                    [handler.handle_state(state) for handler in self.handlers]
                    game_clock = self.clock_handler.get_game_clock()
                    for tracked_event in self.tracked_events:
                        if tracked_event.handle_time(game_clock):
                            self.speaker.say(tracked_event.get_event_name())

                except queue.Empty:
                    pass
            