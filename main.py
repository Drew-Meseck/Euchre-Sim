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
        print(" {} of {}".format(self.value, self.suit))

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
        for Player in Players:
            for i in range(0, 5):
                c = self.cards.pop()
                Player.hand.append(c)


class Player:
    def __init__(self, i, t):
        self.id = i
        self.team = t
        self.hand = []
        self.tricks = []

    #placeholder for eventual play functions.
    def show_hand(self):
        print("Cards in hand for Player {}: ".format(self.id))
        for card in self.hand:
            card.show()


class Game:
    def __init__(self, p, d):
        self.Players = p
        self.Deck = d
        self.t1_points = 0
        self.t2_points = 0
    
    def step(self):
        pass

    def reset(self):
        self.Deck = generateDeck()
        self.Deck.shuffle()

#setup at the beginning of the game
def setup_macro():

    #creates 4 players, two on each team
    p1 = Player(1, 0)
    p2 = Player(2, 1)
    p3 = Player(3, 0)
    p4 = Player(4, 1)
    #creates array of players
    Players = [p1, p2, p3, p4]

    deck = generateDeck()

    game = Game(Players, deck)
    #game.Deck.show()
    game.Deck.shuffle()
    game.Deck.show()
    game.Deck.deal(game.Players)
    print("\n")

    for p in game.Players:
        p.show_hand()
        print("\n")

#setup for each round
def setup_micro():
    pass

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
    setup_macro()


 



if __name__ == "__main__":
    main()

