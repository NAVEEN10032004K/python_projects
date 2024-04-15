import random
import math

def guessing_game():
    lower_bound = int(input("Enter the lower range: "))  # The upper bound for the range
    upper_bound = int(input("Enter the upper range: "))  # The lower bound for the range

    actual_number = random.randint(lower_bound, upper_bound)  # The minimum required guesses

    required_guess = round(math.log(upper_bound - lower_bound + 1, 2))
    print("\n\tYou've only ", required_guess, " chances to guess the integer!")
    count = 0  # The number of guesses set to 0

    while count < required_guess:
        count += 1  # The number guesses incremented by 1 for every guess

        guess = int(input("Enter the guess: "))

        if guess == actual_number:
            print(f"Congratulation you guessed the number in the {count} guess.")
            break

        elif guess < actual_number:
            print("Guessed number is small!!!")

        elif guess > actual_number:
            print("Guessed number is big!!")

    # If user did too many guesses print this
    if count >= required_guess:
        print("Opps too many guess.")
        print(f"The actual number is {actual_number}")

def main():
    guessing_game()

if __name__ == '__main__':
    main()
