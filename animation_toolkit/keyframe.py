from enum import Enum, auto

from .transform import Transform

class KeyFrame: 
    class Ease(Enum):
        INSTANT = auto()
        LINEAR = auto()
        EXPONENTIAL = auto()
    def __init__(self, transform=Transform(), ease=Ease.LINEAR):
        self.transform, self.ease = transform, ease
    def __repr__(self) -> str:
        return f"KeyFrame({self.transform}, {self.ease})"
