from dataclasses import dataclass

@dataclass
class Event:
    name: str
    amount: int
    sentence: str
    offset: int = 15
    recurring: bool = True
    
    @classmethod
    def create_from_dict(cls, **kwarg):
        return Event(**kwarg)