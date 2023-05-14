from components.countdown import CountDown
from components.event import Event
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

speaker = Speaker()
speaker.say("Counters are set!")


try:
    while True: 
        game_clock = server.q.get()

        if game_clock is None: 
            print("Emty event queue")
            continue
        log.debug(game_clock)
        for countdown in countdowns:
            if countdown.handle_time(game_clock):
                print(game_clock)
                speaker.say(countdown.get_event_name())

except KeyboardInterrupt:
    log.info("Interruption signal sent.")
    server.stop()
    speaker.stop()
    log.info("Program stopped")
    pass