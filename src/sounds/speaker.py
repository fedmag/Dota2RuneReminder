import pyttsx3

class Speaker:

    def __init__(self) -> None:
        self.tts = pyttsx3.init()
        

    def say(self, sentence: str) -> None:
        print(f"Saying: {sentence}")
        self.tts.say(sentence)
        self.tts.runAndWait()