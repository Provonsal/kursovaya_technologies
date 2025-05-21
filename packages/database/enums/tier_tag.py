from collections import namedtuple
from enum import Enum

TIER_LEVELS = namedtuple('TIER_LEVELS', ['first', 'second', 'third', 'fourth'])

TIER_LEVELS = TIER_LEVELS(1,2,3,4)

class OfferTier(Enum):
    T1 = None
    T2 = None
    T3 = None
    T4 = TIER_LEVELS
    T5 = TIER_LEVELS
    T6 = TIER_LEVELS
    T7 = TIER_LEVELS
    T8 = TIER_LEVELS
    