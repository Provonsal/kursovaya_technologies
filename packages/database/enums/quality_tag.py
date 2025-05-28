from enum import Enum, auto


class OfferQuality(str, Enum):
    Normal = "Normal"
    Good = "Good"
    Outstanding = "Outstanding"
    Excellent = "Excellent"
    Masterpiece = "Masterpiece"