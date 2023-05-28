from dota2remainder import Dota2RuneRemainder
from utils.utils import generate_alternative_icon, gsi_files_are_in_place, prepare_for_gsi_integration

from typing import Dict
import pystray
from PIL import Image
import toml
import logging
import os

logging.basicConfig(level=logging.INFO)
logging.getLogger("comtypes").setLevel(logging.WARNING)
log = logging.getLogger(__name__)

log.info(f"WDR: {os.getcwd()}")
with open("resources/config.toml", "r") as file:
    config: Dict = toml.load(file)

if __name__ == "__main__":
    
    try:
        icon_img = Image.open("resources/icon.ico")
    except:
        log.warning("Unable to open icon file. Generating icon.")
        icon_img = generate_alternative_icon(64, 64, 'black', 'white')
        
    if gsi_files_are_in_place(config["general"]["dota2path"]): log.info("Files for gsi were found!")
    else: 
        log.info("Files for gsi not found.. creating..")
        prepare_for_gsi_integration(config["general"]["dota2path"])
        result = gsi_files_are_in_place(config["general"]["dota2path"])
        log.info(f"Files created: {result}")
        

    dota2remainder = Dota2RuneRemainder(config)
    
    def start(): 
        if not dota2remainder.is_running(): dota2remainder.change_running_state(True)
        
    def stop(): 
        if dota2remainder.is_running(): dota2remainder.change_running_state(False)
        
    def exit_program():
        if dota2remainder.is_running(): stop()
        icon.stop()
        os._exit(1)
    
    icon = pystray.Icon(
        name='Doata2RuneRemainder',
        icon=icon_img
    )

    icon.menu = (
        pystray.MenuItem("Start", start, default=True),
        pystray.MenuItem("Stop", stop),
        pystray.MenuItem("Exit", exit_program),
    )
    icon.run()