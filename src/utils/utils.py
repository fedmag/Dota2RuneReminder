from PIL import Image, ImageDraw
import os
import logging

log = logging.getLogger(__name__)


def generate_alternative_icon(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)
    return image


def gsi_files_are_in_place(dota_path: str) -> bool:
    return os.path.isfile(
        os.path.join(
            dota_path,
            "cfg\\gamestate_integration",
            "gamestate_integration_py.cfg"
            )
        )


def prepare_for_gsi_integration(dota_path: str):
    cfg_content = """"Python Dota 2 GSI Integration"
    {
        "uri"       "http://localhost:3000"
        "timeout"   "5.0"
        "buffer"    "0.1"
        "throttle"  "0.1"
        "heartbeat" "30.0"
        "data"
        {
            "provider"  "1"
            "map"       "1"
            "player"    "1"
            "hero"      "1"
            "abilities" "1"
            "items"     "1"
        }
    }"""
    filepath = os.path.join(dota_path, "cfg\\gamestate_integration")
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open(filepath + "\\gamestate_integration_py.cfg", "a") as file:
        file.write(cfg_content)
