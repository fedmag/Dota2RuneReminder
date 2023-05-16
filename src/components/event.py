import pyttsx3

class Event:

    def __init__(self, name: str, amount: float, recurring: bool = True) -> None:
        self.name = name
        self.amount = amount
        self.recurring = recurring
        self.tts = pyttsx3.init()
        self.tts.runAndWait()


    def alarm(self):
        print(f"emitting sound for {self.name}")
        self.tts.say(self.name)