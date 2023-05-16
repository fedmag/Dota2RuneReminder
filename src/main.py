from components.countdown import CountDown
from components.event import Event
from components.event_handlers.clock_handler import ClockEventHandler
from sounds.speaker import Speaker
from gsi.server import ServerManager
from queue import Queue
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("comtypes").setLevel(logging.WARNING)
log = logging.getLogger(__name__)

def run():
    tracked_events = [
        CountDown(Event("Lotus and gold runes spawning in 15 seconds", 3*60)), 
        CountDown(Event("Wisdom rune spawning 15 seconds", 7*60)),
        CountDown(Event("Tormentor spawned", 20*60, recurring = False)) # a one time event as there is no way of knowing when it is killed
    ]

    server = ServerManager(q = Queue())
    server.start()

    clock_handler = ClockEventHandler()
    handlers = [
        clock_handler
    ]

    speaker = Speaker()
    speaker.say("Counters are set!")


    try:
        while True: 
            state: str = server.q.get()
            [handler.handle_state(state) for handler in handlers]
            game_clock = clock_handler.get_game_clock()
            for tracked_event in tracked_events:
                if tracked_event.handle_time(game_clock):
                    speaker.say(tracked_event.get_event_name())

    except KeyboardInterrupt:
        log.info("Interruption signal sent.")
        server.stop()
        speaker.stop()
        log.info("Program stopped")
        pass

if __name__ == "__main__":
    run()