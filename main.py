#Main File

import numpy as np
import tkinter as tk
import random




#Class definitions
class Card:
    def __init__(self, val, su):
        self.value = val
        self.suit = su

    def show(self):
        print(" {} of {} \n".format(self.value, self.suit))

class Deck:
    def __init__(self, c):
        self.cards = c

    def shuffle(self):
        temp = []
        while self.cards:
             r = random.randint(0, len(self.cards) - 1)
             n = self.cards.pop(r)
             temp.append(n)

        self.cards = temp



    def show(self):
        for card in self.cards:
            card.show()

    def deal(self, Players):
        pass

class Player:
    def __init__(self, t):
        self.team = t
        self.hand = []
        self.tricks = []

    #placeholder for eventual play functions.

class Game:
    def __init__(self, p, d):
        self.Players = p
        self.Deck = d
        self.t1_points = 0
        self.t2_points = 0
    
    def step(self):
        pass

    def reset(self):
        pass

def setup():

    #creates 4 players, two on each team
    p1 = Player(0)
    p2 = Player(1)
    p3 = Player(0)
    p4 = Player(1)
    #creates array of players
    Players = [p1, p2, p3, p4]

    deck = generateDeck()

    game = Game(Players, deck)
    #game.Deck.show()
    game.Deck.shuffle()
    game.Deck.show()

def generateDeck():
    values = ["9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    cards = []

    for value in values:
        for suit in suits:
            c = Card(value, suit)
            cards.append(c)

    return Deck(cards)
    


#Main function
def main():
    setup()






if __name__ == "__main__":
    main()

