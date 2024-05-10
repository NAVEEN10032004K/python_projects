from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
print("HelloWorld, I'm Naveen and Welcome to the Number_Guessing_Game!")
print("I am thinking a number between 1 - 100, Can you Guess? ")


def generate_number():
    """Generate random number between 1 - 50"""
    number = random.randint(1, 100)
    return number


random_number = generate_number()

level = input("Choose you level, type 'easy' or type 'hard': ")

if level == "easy":
    difficulty = 9
    while True:

        guess = int(input("Make a Guess: "))
        if guess == random_number:
            print(f"Your guess is correct, I was thinking of {random_number}")
            break
        elif guess > random_number:
            print("You are guessing too high. ")
            print(f"You left with {difficulty} guesses,")
            difficulty -= 1
        elif guess < random_number:
            print("You are guessing too low. ")
            print(f"You left with {difficulty} guesses,")
            difficulty -= 1
        if difficulty < 0:
            print(f"Oops! you loose, I was thinking about {random_number}")
            break

elif level == "hard":
    difficulty = 4
    while True:

        guess = int(input("Make a Guess: "))
        if guess == random_number:
            print(f"Your guess is correct, I was thinking of {random_number}")
            break
        elif guess > random_number:
            print("You are guessing too high. ")
            print(f"You left with {difficulty} guesses,")
            difficulty -= 1
        elif guess < random_number:
            print("You are guessing too low. ")
            print(f"You left with {difficulty} guesses,")
            difficulty -= 1
        if difficulty < 0:
            print(f"Oops! you loose, I was thinking about {random_number}.")
            break

