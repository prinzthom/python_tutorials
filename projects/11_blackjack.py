import random
from random import choice

def deal_cards():
    count=0
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    while count<=2:
        for card in cards:
            card = random.choice(cards)
            count+=1
            return card

def draw_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def comp_draw_card(computer_score):
    if computer_score<17 and computer_score !=0:
        return "draw"

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
    #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "it's a draw"
    elif computer_score == 0:
        return "you lose, you'r opponent has Blackjack"
    elif player_score == 0:
        return "you Win, you have Blackjack"
    if player_score > 21 and computer_score > 21:
        return "You went over 21. You lose"
    elif player_score > 21:
        return "You went over 21. You lose"
    elif computer_score > 21:
        return "you'r opponenr went over. You win"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"
    """Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins. If you and the computer are both over 21, then you lose!"""

def check_game_conditions(player_score,computer_score):
    if player_score == 0 or computer_score == 0 or player_score > 21:
        return "gameover"


def play_game():
    # Deal the user and computer 2 cards each using deal_card()
    print("Weelcome to Blackjack")
    player_hand=[]
    computer_hand=[]
    gameover=False

    player_hand.append(deal_cards())
    computer_hand.append(deal_cards())



    while gameover==False:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"your hand:{player_hand}, your current score:{player_score}")
        print(f"your hand:{computer_hand}, your current score:{computer_score[0]}")
        
        
        if check_game_conditions(player_score,computer_score)=="gameover":
            gameover=True
        else:
            choice=input("would you like to HIT or STAND :")
            if choice==("hit"):
                player_hand.append(draw_card())
            else:
                gameover=True

    while comp_draw_card(computer_score)=="draw":
        computer_hand.append(draw_card())
        computer_score = calculate_score(computer_hand)
    print(compare(player_score, computer_score))
    print(f"Your hand: {player_hand}, you'r final score: {player_score}")
    print(f"Computer's hand: {computer_hand}, Computer's final score: {computer_score}")
    print("---------GAME OVER---------")

play_game()
