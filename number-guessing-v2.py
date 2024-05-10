from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""



def check_answer(answer, guess, chances):
    """checks the answer against the guess and tells how many turns left"""
    if guess == answer:
        print(f"You are right, I was thinking about {answer}.😀")
    elif guess > answer:
        print("Too high.")
        return chances - 1
    elif guess < answer:
        print("Too low.")
        return chances - 1

def difficulty():
    level = input("Choose your level, type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

def main():
    print(logo)
    print("HelloWorld, I'm Naveen and Welcome to the Number_Guessing_Game!")
    print("I am thinking a number between 1 - 100, Can you Guess? ")
    actual_number = randint(1, 100)
    chances = difficulty()
    guessed_number = 0
    while guessed_number != actual_number:
        print(f"You have {chances} left to guess the correct number. ")
        guessed_number = int(input("Guess the number I am thinking of: "))
        chances = check_answer(answer=actual_number, guess=guessed_number, chances=chances)
        if chances == 0 :
            print("You ran out of chances, you lose,")
            return
        elif actual_number != guessed_number:
            print("Make another guess.")

main()
