from components.countdown import CountDown
from components.event import Event
from sounds.speaker import Speaker
from gsi.server import ServerManager
from threading import Thread
from queue import Queue



countdowns = [
    CountDown(Event("lotus and gold runes spawning", 5)), 
    CountDown(Event("wisdom rune spawning", 20))
]

server = ServerManager(q = Queue())
server.start()
# thread = Thread(target=server.start, args=(event_queue,))
# thread.start()


speaker = Speaker()
speaker.say("Counters are set!")


try:
    while True: 
        game_clock = server.q.get()
        for countdown in countdowns:
            if countdown.handle_time(game_clock):
                print(game_clock)
                speaker.say(countdown.get_event_name())
        pass


except KeyboardInterrupt:
    print("Interruption signal sent.")
    server.stop()
    print("Program stopped")
    pass