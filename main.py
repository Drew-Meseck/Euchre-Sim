#Main File

import numpy as np
import tkinter as tk
from objects import Game, Deck, Player, Card


#setup at the beginning of the game
def setup_macro():

    #creates 4 players, two on each team
    p1 = Player(1, 0)
    p2 = Player(2, 1)
    p3 = Player(3, 0)
    p4 = Player(4, 1)
    #creates array of players
    Players = [p1, p2, p3, p4]


    #generates deck and creates the game object
    deck = Deck()

    game = Game(Players, deck)
    game.Deck.show()
    game.Deck.deal(game.Players)
    print("\n")

    for p in game.Players:
        p.show_hand()
        print("\n")

    print("The Card Flipped Up is: ")
    to_call = game.Deck.cards[0]
    to_call.show()

    print("The Dealer for this round is: ")
    dealer = game.Players[3]
    dealer.show()

#setup for each round
def setup_micro(game):
    game.reset()
    game.Deck.deal(game.Players)
    game.shiftDealer()
    


    
#Main function
def main():
    setup_macro()


 



if __name__ == "__main__":
    main()

