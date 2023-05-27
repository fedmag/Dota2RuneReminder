from dota2remainder import Dota2RuneRemainder

from typing import Dict
import pystray
from PIL import Image, ImageDraw
import toml
import logging
import os

logging.basicConfig(level=logging.INFO)
logging.getLogger("comtypes").setLevel(logging.WARNING)
log = logging.getLogger(__name__)
config: Dict = toml.load("resources/config.toml")

if __name__ == "__main__":

    def create_image(width, height, color1, color2):
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.rectangle(
            (width // 2, 0, width, height // 2),
            fill=color2)
        dc.rectangle(
            (0, height // 2, width // 2, height),
            fill=color2)
        return image
    
    dota2remainder = Dota2RuneRemainder(config)
    
    def start():
        print("start")
        dota2remainder.change_running_state(True)
        
    def stop():
        print("stop")
        dota2remainder.change_running_state(False)
        
    def exit_program():
        print("exit")
        dota2remainder.change_running_state(False)
        print("exiting icon")
        icon.stop()
        os._exit(1)
    
    
    icon = pystray.Icon(
        name='Doata2RuneRemainder',
        icon=create_image(64, 64, 'black', 'white')
    )

    # Define the menu items
    icon.menu = (
        pystray.MenuItem("Start", start),
        pystray.MenuItem("Stop", stop),
        pystray.MenuItem("Exit", exit_program),
    )
    icon.run()