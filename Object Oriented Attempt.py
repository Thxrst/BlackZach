import time
import random


class Game:
    def __init__(self):
        self.players = []
        self.decks = 0
        self.min_bet = 50
        self.max_bet = 100
    def play(self):
        pass

class Deck:
    def __init__(self,number_of_decks = 1):
        self.deck = []