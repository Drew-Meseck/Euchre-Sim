import random
import pygame

#Class definitions
class Card:
    def __init__(self, val, su):
        self.value = val
        self.suit = su

    def show(self):
        print(" {} of {}".format(self.value, self.suit))

class Deck:
    
    def __init__(self):
        self.cards = self.generateDeck()
        self.sprites = pygame.sprite.Group()

    def generateDeck(self):
        values = ["9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        cards = []

        for value in values:
            for suit in suits:
                c = Card(value, suit)
                cards.append(c)

        return cards

    def show(self):
        for card in self.cards:
            card.show()

    def deal(self, Players):
        for Player in Players:
            while len(Player.hand) < 5:
                c = random.choice(self.cards)
                self.cards.remove(c)
                Player.hand.append(c)

    def update_deck():
        #update the sprites in the deck


class Player:
    def __init__(self, i, t):
        self.id = i
        self.team = t
        self.hand = []
        self.tricks = []
        self.sprites_hand = pygame.sprite.Group()

    #placeholder for eventual play functions.
    def show_hand(self):
        print("Cards in hand for Player {}: ".format(self.id))
        for card in self.hand:
            card.show()
    
    def show(self):
        print("Player {} on team {}".format(self.id, self.team))

    def update_hand():
        #update the sprites in hand

class Game:
    def __init__(self, p, d):
        self.Players = p
        self.Deck = d
        self.t0_points = 0
        self.t1_points = 0
        self.t0_tricks = 0
        self.t0_tricks = 0

    def shiftDealer(self):
        #ensures that the new dealer is alwyas in position 3 after each round so that the loop is the initial order of play
        new_dealer = self.Players.pop(0)
        self.Players.append(new_dealer)
    
    def step(self):
        pass

    def reset(self):
        self.Deck = Deck()
        for Player in self.Players:
            Player.hand = []
        self.t0_tricks = 0
        self.t1_tricks = 0
        
