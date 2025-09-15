from asciiart8 import logo11
import random
import os

def new_Ran_card(hand):
    hand.append(random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))

def compare(dealer_hand, player_hand):  
    if (sum(dealer_hand)) > 21 :
        print(f"The dealer hand is {dealer_hand} with the score :{sum(dealer_hand)}\n !!!!!! YOU WIN !!!!!! ")
    elif (21 - sum(dealer_hand)) < (21 - sum(player_hand)) :
        print(f"The dealer hand is {dealer_hand} with the score :{sum(dealer_hand)}\n !!!!!! YOU LOSE !!!!!! ")
    elif (21 - sum(dealer_hand)) > (21 - sum(player_hand)) :
        print(f"The dealer hand is {dealer_hand} with the score :{sum(dealer_hand)}\n !!!!!! YOU WIN !!!!!! ")
    else:
        print(f"The dealer hand is {dealer_hand} with the score :{sum(dealer_hand)}\n !!!!!! NO WINNER !!!!!! ")

player_again = "y" 
while player_again == 'y':
    print(logo11)
    player_hand = []
    dealer_hand = []
    new_Ran_card(player_hand)
    new_Ran_card(player_hand)
    new_Ran_card(dealer_hand)
    new_Ran_card(dealer_hand)

    print(f"Your hand is {player_hand} with the score : {sum(player_hand)}")
    if 11 in player_hand and sum(player_hand) > 21 : 
        player_hand[player_hand.index(11)] = 1
        print(f"As you have an ace and Your hand is greater than 21 \n you new hand is {player_hand} with the score : {sum(player_hand)}")

    print(f"The dealer first card is {dealer_hand[0]}")
    hit = input("Enter'y' to hit or 's' to stand.")
    if hit == "y":
        new_Ran_card(player_hand)
        print(f"Your hand is now {player_hand} with the score : {sum(player_hand)}")
        if player_hand[2] == 11  and sum(player_hand) > 21 : 
            player_hand[2] = 1
            print(f"As you have an ace and Your hand is greater than 21 \n you new hand is {player_hand} with the score : {sum(player_hand)}")
    if sum(player_hand) > 21:
        print(f"The dealer hand is {dealer_hand} with the score :{sum(dealer_hand)}\n !!!!!! LOSE !!!!!! ")
    elif sum(dealer_hand) > 21 :
        print(f"The dealer hand is {dealer_hand} with the score :{sum(dealer_hand)}\n !!!!!! YOU WIN !!!!!! ")
    elif sum(dealer_hand) < 16 :
        new_Ran_card(dealer_hand)
        if 11 in dealer_hand and sum(dealer_hand) > 21 :
            dealer_hand[dealer_hand.index(11)] = 1
        compare(dealer_hand, player_hand)
    else:
        compare(dealer_hand, player_hand)
    player_again = input("Enter 'y' to play again:  ")
    if player_again == 'y':
        os.system("clear")