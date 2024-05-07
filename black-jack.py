import random

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
print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_card = []
is_game_over = False
for _ in range(2):
    user_cards.append(deal_card())
    computer_card.append(deal_card())

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!!"
    elif computer_score == 0:
        return "Lose, computer has BlackJack."
    elif user_score == 0:
        return "You Win, you have a BlackJack."
    elif computer_score > 21:
        return "You Win, computer went over."
    elif user_score > 21:
        return "You lose, you went over."
    elif user_score > computer_score:
        return "You win!!"
    else:
        print("You lost!!")
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_card)
    print(f" Your card are: {user_cards}, current score: {user_score}")
    print(f" Computer's first card is: {computer_card[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_deal_another_card = input("Type 'y' to continue or 'n' to pass:  ")
        if user_deal_another_card == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)

print(f"  Your final hand is {user_cards}, and your final score is {user_score}")
print(f"  computer's final hand is {computer_card}, and computer's final score is {computer_score}")
print(compare(user_score, computer_score))

