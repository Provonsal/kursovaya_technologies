from enum import Enum, auto


class OfferQuality(str, Enum):
    Normal = auto()
    Good = auto()
    Outstanding = auto()
    Excellent = auto()
    Masterpiece = auto()