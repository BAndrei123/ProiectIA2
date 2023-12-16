import random
from enum import Enum

from pythonProject2.constants import CARDS

class GameState(Enum):
    START = "Start"
    AUCTION = "Auction"
    TRUMP_SEL = "Trump Selection"
class Deck:

    def __init__(self):
        self.cards = CARDS

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, number_of_cards):
        cards = []
        for _ in range(0, number_of_cards):
            cards.append(self.cards.pop())
        return cards


class GameEngine:
    deck = None
    current_player = None
    players = None
    points = None
    state = None

    def __init__(self, player1, player2, player3, player4):
        self.deck = Deck()
        self.players = [player1, player2, player3, player4]
        self.points = {1: 0, 2: 0}
        self.state

