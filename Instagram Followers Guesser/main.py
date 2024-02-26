from Game_data import data
import random

def format_date(account):
    account_name = account["name"]
    # account_followers = account["followers"]
    return f"{account_name}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(" *****************\U0001F4A5 Instagram f-ollowers\U0001F49A Guesser \U0001F4A5 ***************** \n")
print(" *************** Who Has More Followers On Instagram ?  **************** ")

score = 0
account_b = random.choice(data)

# get random data from Game_data..
continue_game = True
while continue_game:
    account_a = account_b
    # if a & b are same again choose.. 
    while account_a == account_b:
        account_b = random.choice(data)

    a_followers_count = account_a["followers"]
    b_followers_count = account_b["followers"]
    print("_______________________________________________________________________\n")
    print(f"Compare\U0001F170 \U0001F449 {format_date(account_a)}         Against\U0001F171 \U0001F449 {format_date(account_b)}")
    
    # ask user for a guess..
    # Who has more followers on Instagram ? 
    guess = input("Option:\U0001F170  or Option:\U0001F171").lower()
    print()
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # check if user is correct
    if is_correct:
        score += 1
        print("\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2")
        print(f"\U0001F7E2    \U0001F973  Yes! You Are Right  \U0001F973    \U0001F7E2")
        print("\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2\U0001F7E2")
        # print("\U0001F600")
        print("_______________________________________________________________________")
    else:
        continue_game = False
        print("\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534")
        print(f"\U0001F534   \U0001F61E  Sorry! you are wrong  \U0001F61E   \U0001F534")
        print("\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\U0001F534\n")
        print("\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973")
        print(f"\U0001F973   \U0001F947    Your Score  : {score}    \U0001F947    \U0001F973")
        print("\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\U0001F973\n")


        
