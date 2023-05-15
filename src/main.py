from components.countdown import CountDown
from components.event import Event
from components.event_handlers.clock_handler import ClockEventHandler
from components.event_handlers.handlers_manager import HandlerManager
from sounds.speaker import Speaker
from gsi.server import ServerManager
from threading import Thread
from queue import Queue
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)




countdowns = [
    CountDown(Event("lotus and gold runes spawning in 15 seconds", 3*60)), 
    CountDown(Event("wisdom rune spawning 15 seconds", 7*60))
]

server = ServerManager(q = Queue())
server.start()

handlerManager = HandlerManager()
handlerManager.add_handler(ClockEventHandler())

speaker = Speaker()
speaker.say("Counters are set!")


try:
    while True: 
        
        handlerManager.handle_event(server.q.get())
        for countdown in countdowns:
            if countdown.handle_time(1):
                speaker.say(countdown.get_event_name())

except KeyboardInterrupt:
    log.info("Interruption signal sent.")
    server.stop()
    speaker.stop()
    log.info("Program stopped")
    pass