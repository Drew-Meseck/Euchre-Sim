#Main File

import numpy as np
import pygame
import sys
sys.path.append(".")

from game_objects import Card, Deck, Player, Game



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
    deck = game_objects.Deck()

    game = gameobjects.Game(Players, deck)
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
    #Get pygame to do what I want it to do.
    pygame.init()
    frames_per_second = 30
    window_height = 600
    window_width = 1200

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    display = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    

    while True:
        clock.tick(frames_per_second)
        
        display.fill(WHITE)



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

    

    #setup_macro()


 



if __name__ == "__main__":
    main()

