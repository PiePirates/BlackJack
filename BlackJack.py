#Import module(s) needed.
import random as rand

#dictionary where numbers 1 - 13 are keys for the names of cards
cards_to_pictures = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}

#defining what will happen when the user inputs hit on a given turn
def player_hit(player_total):
    #1 refers to the ace, 2-10 refer to the cards 2-10, 11 refers to the Jack, 12 refers to the Queen, 13 refers to the King 
    possibilities = rand.randint(1, 13)
    #add card type to a list
    players_cards.append(cards_to_pictures[possibilities])
    #Logic for Kings, Queens, and Jacks
    if possibilities >= 11:
        player_total += 10
    #Logic for cards 2-10
    elif possibilities >= 2:
        player_total += possibilities 
    #Logic for Ace's
    else:
        player_total += 11
        player_ace_counter.append(cards_to_pictures[possibilities])
    return player_total

#defining what will happen every time the dealer hits
def dealer_hit(dealer_total):
    #1 refers to the ace, 2-10 refer to the cards 2-10, 11 refers to the Jack, 12 refers to the Queen, 13 refers to the King 
    possibilities = rand.randint(1, 13)
    #add card type to a list
    dealers_cards.append(cards_to_pictures[possibilities])
    #Logic for Kings, Queens, and Jacks
    if possibilities >= 11:
        dealer_total += 10
    #Logic for cards 2-10
    elif possibilities >= 2:
        dealer_total += possibilities 
    #Logic for Ace's
    else:
        dealer_total += 11
        dealer_ace_counter.append(cards_to_pictures[possibilities])
    return dealer_total

#print the gamestate
def print_gamestate(dealers_cards, players_cards):
    print("~~~~~~~~~~~~~~~~~~~~")
    print("The dealers hand is:")
    for i in range(len(dealers_cards)):
        print(dealers_cards[i])
    print("")
    print("The players hand is:")
    for i in range(len(players_cards)):
        print(players_cards[i])
    print("~~~~~~~~~~~~~~~~~~~~")
#Create a welcome message to my program!
print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|  _ \| |        /\   / ____| |/ /   | |  /\   / ____| |/ /     \ \    / / /_ |
| |_) | |       /  \ | |    | ' /    | | /  \ | |    | ' /       \ \  / /   | |
|  _ <| |      / /\ \| |    |  < _   | |/ /\ \| |    |  <         \ \/ /    | |
| |_) | |____ / ____ \ |____| . \ |__| / ____ \ |____| . \         \  /     | |
|____/|______/_/    \_\_____|_|\_\____/_/    \_\_____|_|\_\         \/      |_|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
By: Baby Singh                                                                               
""")

playing_game = True
while playing_game:
#Logic for the dealers and the players turns. This Includes the initial conditions for the game.
    dealers_cards = []
    players_cards = []
    dealer_ace_counter = []
    player_ace_counter = []
    dealer_total = dealer_hit(0)
    player_total = player_hit(0) + player_hit(0)
    dealers_turn = False
    players_turn = False
#First player input, determines if the game starts or ends.
    print("")
    player_input = input("Hello welcome to BlackJack V1! Type \"play\" to get the game started or type \"quit\" to quit. ")
    if player_input == "play":
        players_turn = True
    elif player_input == "quit":
        playing_game = False
        print("Thanks for playing my game!")
    else:
        print("What you inputed is not valid, try again.")
    
    while players_turn:
        #print a visual to see your own cards as well as 
        print_gamestate(dealers_cards, players_cards)
        #User input for each turn of the game.
        choice = input("Would you like to \"hit\" or \"stay\"? ")
        if choice == "hit":
            player_total = player_hit(player_total)    
        elif choice == "stay":
            print("You chose to stay")
            players_turn = False
            dealers_turn = True
        else:
            print("What you inputed is not valid, try again.")
        
        if player_total > 21:
            if "Ace" in player_ace_counter:
                player_total -= 10
                player_ace_counter.pop(-1)
            
            else:
                print_gamestate(dealers_cards, players_cards)
                print("The player has gone bust! You lose!")
                players_turn = False


#When the player's turn is over we now need the dealer to play
    while dealers_turn:
        dealer_total = dealer_hit(dealer_total)
        input("Press \"Enter\" to see dealers next card.")
        print_gamestate(dealers_cards, players_cards)
        
        if dealer_total > 21:
                if "Ace" in dealer_ace_counter:
                    dealer_total -= 10
                    dealer_ace_counter.pop(-1)
                else:
                    print_gamestate(dealers_cards, players_cards)
                    print("The dealer has gone bust! You win!")
                    dealers_turn = False
       
        if dealer_total >= 17 or dealer_total >= player_total:
            dealers_turn = False
        #get final results of game if the dealer and or player have not gone bust
        if dealers_turn == False:
            if dealer_total > player_total and dealer_total <= 21: 
                print_gamestate(dealers_cards, players_cards)
                print("The dealer wins!")
            elif dealer_total < player_total:
                print_gamestate(dealers_cards, players_cards)
                print("The player wins!")
            elif dealer_total == player_total:
                print_gamestate(dealers_cards, players_cards)
                print("It's a draw!")
            else:
                pass


    





