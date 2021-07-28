using Base: String, Int8, Bool, Iterators
using Printf

@enum Suit spade = 1 club diamond heart

@enum Rank nine = 1 ten jack queen king ace

struct Card
    rank::Rank
    suit::Suit
end

mutable struct Player
    cards::AbstractVector{Card}
    id::Int8
    team::Bool
    tricks::Int8
end



function init_deck()
    println("initializing deck...\n")
    deck = AbstractVector{Card}
    for i in instances(Suit)
        for j in instances(Rank)
            card = Card(j, i)
        end
    end
    println()
    return deck        
end

function setup()
    println("setting up...\n")
    deck = init_deck()
    return deck
end


function main()
    print("Welcome to the Euchre Simulation\n")
    deck = setup()
    #how to iterate over vectors to print the deck for testing?

end

main()