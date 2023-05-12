from components.countdown import CountDown
from components.event import Event
from sounds.speaker import Speaker


countdowns = [
    CountDown(Event("lotus and gold runes", 3*60)), 
    CountDown(Event("wisdom rune", 7*60))
]

speaker = Speaker()
try:
    while True: 
        for countdwn in countdowns:
            if (countdwn.should_sound_alarm()):
                speaker.say(countdwn.get_event_name())


except KeyboardInterrupt:
    print("Interruption signal sent.")
    pass