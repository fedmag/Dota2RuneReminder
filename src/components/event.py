from dataclasses import dataclass

@dataclass
class Event:
    name: str
    amount: int
    recurring: bool = True