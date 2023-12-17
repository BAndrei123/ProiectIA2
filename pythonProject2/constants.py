from enum import Enum

CARDS = ["bc10", "bc2", "bc3", "bc4", "bc9", "bca", "fc10", "fc2", "fc3", "fc4", "fc9", "fca", "gc10", "gc2", "gc3",
         "gc4", "gc9", "gca", "rc10", "rc2", "rc3", "rc4", "rc9", "rca"]


class Suit(Enum):
    RED = 'r'
    GREEN = 'f'
    ACORN = 'g'
    VAN = 'b'


WINNING_CARD_INPUT_FILENAME = 'winning_card.in'
WINNING_CARD_OUTPUT_FILENAME = 'winning_card.out'

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
