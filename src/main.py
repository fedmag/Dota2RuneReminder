
from countdown import CountDown
from event import Event

countdowns = [CountDown(Event("lotus rune", 5)), CountDown(Event("wisdom rune", 10))]
try:
    while True:
        for countdown in countdowns:
            if not countdown.is_running:
                countdown.run_timer()
except KeyboardInterrupt:
    print("Interruption signal sent.")
    pass