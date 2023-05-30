from dataclasses import dataclass
from typing import Any


@dataclass
class Map:
    name: str
    matchid: str
    game_time: int
    clock_time: int
    daytime: bool
    nightstalker_night: bool
    radiant_score: int
    dire_score: int
    game_state: str
    paused: bool
    win_team: str
    customgamename: str
    radiant_ward_purchase_cooldown: int
    dire_ward_purchase_cooldown: int
    roshan_state: str
    roshan_state_end_seconds: int

    @staticmethod
    def from_dict(obj: Any) -> 'Map':
        _name = str(obj.get("name"))
        _matchid = str(obj.get("matchid"))
        _game_time = int(obj.get("game_time"))
        _clock_time = int(obj.get("clock_time"))
        _daytime = bool(obj.get("daytime"))
        _nightstalker_night = bool(obj.get("nightstalker_night"))
        _radiant_score = int(obj.get("radiant_score"))
        _dire_score = int(obj.get("dire_score"))
        _game_state = str(obj.get("game_state"))
        _paused = bool(obj.get("paused"))
        _win_team = str(obj.get("win_team"))
        _customgamename = str(obj.get("customgamename"))
        _radiant_ward_purchase_cooldown = int(obj.get("radiant_ward_purchase_cooldown"))
        _dire_ward_purchase_cooldown = int(obj.get("dire_ward_purchase_cooldown"))
        _roshan_state = str(obj.get("roshan_state"))
        _roshan_state_end_seconds = int(obj.get("roshan_state_end_seconds"))
        return Map(_name, _matchid, _game_time, _clock_time, _daytime, _nightstalker_night, _radiant_score, _dire_score,
                   _game_state, _paused, _win_team, _customgamename, _radiant_ward_purchase_cooldown,
                   _dire_ward_purchase_cooldown, _roshan_state, _roshan_state_end_seconds)
