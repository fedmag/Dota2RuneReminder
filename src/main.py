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
    CountDown(Event("Lotus and gold runes spawning in 15 seconds", 3*60)), 
    CountDown(Event("Wisdom rune spawning 15 seconds", 7*60)),
    CountDown(Event("Tormentor spawned", 20*60)) # TODO this is a one time event
]

server = ServerManager(q = Queue())
server.start()

handlerManager = HandlerManager()
handlerManager.add_handler(ClockEventHandler())

clock_handler = ClockEventHandler()

speaker = Speaker()
speaker.say("Counters are set!")


try:
    while True: 
        state: str = server.q.get()
        # handlerManager.handle_event(state)
        clock_handler.handle_event(state)
        game_clock = clock_handler.get_game_clock()
        for countdown in countdowns:
            if countdown.handle_time(game_clock):
                speaker.say(countdown.get_event_name())

except KeyboardInterrupt:
    log.info("Interruption signal sent.")
    server.stop()
    speaker.stop()
    log.info("Program stopped")
    pass