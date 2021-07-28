# Euchre-Sim
An application that utilizes AI to simulate Euchre games in order to aggregate data about the game generally.

This program is written in Julia and will simulate both individual games of euchre as well as a special version of the euchre tournament performed at the Bunek Reunion in Michigan. 

The rules of euchre being used here:

 - 24 card deck (anything below a 9 not including aces are omitted [9, 10, J, Q, K, A])
 - Trump suit will have a jack high, with the other jack of the same color being the second highest, hierarchy then proceeds as A, K, Q, 10, 9
 - Trump suits always beat non-trump suits
 - The suit that is led must be followed if the player has that suit in their hand
 - Calling trump will consist of two rounds
    - the first is constrained to the selection of a single card that will be added to the dealers hand if called, the suit of that card then becomes trump for the round
    - the second round is available to any suit other than the one turned down, no cards are picked up or discarded


Simulation steps:

1) Set up the game
    - Create the Players and give them partners
    - Initialize the deck and shuffle it.
    - deal out 20 cards, 5 cards to 4 players
    - look at the top card

2) Calling Trump
    - Starting with the player left of the dealer - they check to see if they want to call up the card... this is where either AI or something will be useful
    - If the card is called up the dealer must replace that card with a card in their hand.

