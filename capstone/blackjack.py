# 2 player game of blackjack
# basic rules:
# - each player starts with 2 cards
# - each card has a value (2-10 are worth their face value, J/Q/K are worth 10, and A can be worth 1 or 11)
# - the player that has the highest total value of cards without going over 21 wins
# - if a player goes over 21, they lose
# - the dealer (computer) must draw cards until they have at least 17 points
# - if the player and dealer have the same total value, it's a tie
# - the player can choose to "hit" (draw another card) or "stand" (keep their current hand)
import random
from enum import Enum
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
max_number = 21
max_dealer = 17

class Choice(Enum):
    STAND = 'n'
    HIT = 'y'


def blackjack():
    should_continue = True
    while should_continue:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        
        if play.lower() == "y":
            player_cards = [random.choice(card), random.choice(card)]
            dealer_cards = [random.choice(card), random.choice(card)]
            
            make_a_choice = True
            while make_a_choice: 
                print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
                print(f"Computer's first card: {dealer_cards[0]}")
                choice = input("Type 'y' to get another card, type 'n' to pass:")
                if choice == Choice.HIT.value:
                    player_cards.append(random.choice(card))
                else: 
                    while sum(dealer_cards) < 17: 
                        dealer_cards.append(random.choice(card))
                    make_a_choice = False

            # if 
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
            if sum(player_cards) < sum(dealer_cards) <= max_number:
                print("you lose")
            elif sum(player_cards) == sum(dealer_cards):
                print("draw")
            elif max_number >= sum(player_cards) > sum(dealer_cards):
                print("You win")

        else:
            should_continue = False  # this exits the loop

# Incomplete code, need to add logic for handling Aces (11 or 1) and checking for busts (going over 21)
blackjack()
