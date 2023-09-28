import random
from game_data import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""



print(logo)

def format_data(guess):
    """Format the account data into printable format"""
    account_name = guess["name"]
    account_disc = guess["description"]
    account_country = guess["country"]
    return f"{account_name}, a {account_disc}, from {account_country}"

def cheak_answer(your_guess, a_followers, b_followers ):
    """use to cheaq the answer"""
    if a_followers > b_followers:
        return your_guess == "a"
    else:
        return  your_guess == "b"


score = 0
game_contiinue_until = True
guess_b = random.choice(data)

while game_contiinue_until:
    guess_a = guess_b
    guess_b = random.choice(data)

    while guess_a == guess_b:
        guess_b = random.choice(data)

    print(f"compare An: {format_data(guess_a)}.")
    print(vs)
    print(f"compare An: {format_data(guess_b)}.")

    guess_ans = input("who has more followers? type 'A' or type 'B': ").lower()

    a_account_followers = guess_a["follower_count"]
    b_account_followers = guess_b["follower_count"]

    is_correct = cheak_answer(guess_ans, a_account_followers, b_account_followers)

    if is_correct:
        score += 1
        print(f" you're right! your current score is {score}")
    else:
        game_contiinue_until = False
        print(f" wrong! your current score is {score}")
