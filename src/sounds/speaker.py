import pyttsx3
import logging

log = logging.getLogger(__name__)

class Speaker:

    def __init__(self) -> None:
        self.tts = pyttsx3.init()
        

    def say(self, sentence: str) -> None:
        log.info(f"Saying: {sentence}")
        self.tts.say(sentence)
        self.tts.runAndWait()
        
    def stop(self):
        log.info("Stopping tts..")
        self.tts.stop()
        log.info("..tts stopped!")