from collections import namedtuple
from enum import Enum

TIER_LEVELS = namedtuple('TIER_LEVELS', ['first', 'second', 'third', 'fourth'])

TIER_LEVELS = TIER_LEVELS(1,2,3,4)

class OfferTier(Enum):
    T1 = None
    T2 = None
    T3 = None
    T4_0 = 4.0
    T4_1 = 4.1
    T4_2 = 4.2
    T4_3 = 4.3
    T4_4 = 4.4
    T5_0 = 5.0
    T5_1 = 5.1
    T5_2 = 5.2
    T5_3 = 5.3
    T5_4 = 5.4
    T6_0 = 6.0
    T6_1 = 6.1
    T6_2 = 6.2
    T6_3 = 6.3
    T6_4 = 6.4
    T7_0 = 7.0
    T7_1 = 7.1
    T7_2 = 7.2
    T7_3 = 7.3
    T7_4 = 7.4
    T8_0 = 8.0
    T8_1 = 8.1
    T8_2 = 8.2
    T8_3 = 8.3
    T8_4 = 8.4

    