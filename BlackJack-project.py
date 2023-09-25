logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return  0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose, because opponent has blackjack"
    elif user_score == 0:
        return  "win because a blackjack"
    elif user_score >21:
        return "you went over. You lose"
    elif computer_score > 21:
        return "opponent went over. You win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    print (logo)


    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:

        user_score =calculate_score(user_card)
        computer_score =calculate_score(computer_card)

        print(f" your card{user_card}, current score: {user_score}")
        print(f"computer frist card {computer_card[0]} ")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_deal = input("type 'y' for another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score >17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? type 'y' or 'n' ") == "y":
    play_game()