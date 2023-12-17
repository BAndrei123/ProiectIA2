import random
from enum import Enum

import pygame

from pythonProject2.constants import CARDS, SCREEN_WIDTH, SCREEN_HEIGHT


class GameState(Enum):
    AUCTION = 0
    TRUMP_SEL = 1
    ROUND = 2
    END = 3


class Deck:

    cards = None
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
    played_cards = None
    current_player = None
    player1 = None
    player2 = None
    player3 = None
    player4 = None
    points = None
    state = None

    def __init__(self, player1, player2, player3, player4):
        self.deck = Deck()
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.played_cards = []

        self.points = {1: 0, 2: 0}
        self.state = GameState.AUCTION

    def switchPlayer(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        elif self.current_player == self.player2:
            self.current_player = self.player3
        elif self.current_player == self.player3:
            self.current_player = self.player4
        elif self.current_player == self.player4:
            self.current_player = self.player1

    def play(self):
        if self.state == GameState.END:
            return

    def renderScene(self, window):
        window.fill((52, 78, 91))
        font = pygame.font.SysFont('comicsans', 60, True)


        # text = font.render(str(len(gameEngine.player1.hand)) + " cards", True, (255, 255, 255))
        # window.blit(text, (100, 500))

        text = font.render(str(len(gameEngine.player2.hand)) + " cards", True, (255, 255, 255))
        window.blit(text, (700, 500))


class Player:
    hand = None
    name = None

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.deal_cards(3))

    def play(self):
        return self.hand.pop(0)




pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CRUCE")
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

gameEngine = GameEngine(Player("Tudor"), Player("Horea"), Player("Andrei"), Player("Ionut"))

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameEngine.play()
    # fill the screen with a color to wipe away anything from last frame

    pygame.display.update()

    gameEngine.renderScene(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
