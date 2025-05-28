from collections import namedtuple
from enum import Enum

TIER_LEVELS = namedtuple('TIER_LEVELS', ['first', 'second', 'third', 'fourth'])

TIER_LEVELS = TIER_LEVELS(1,2,3,4)

class OfferTier(Enum):
    T1 = None
    T2 = None
    T3 = None
    T4 = (0, 1, 2, 3, 4)
    T5 = (0, 1, 2, 3, 4)
    T6 = (0, 1, 2, 3, 4)
    T7 = (0, 1, 2, 3, 4)
    T8 = (0, 1, 2, 3, 4)
    