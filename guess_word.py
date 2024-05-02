import random

name = input("Enter your name: ")
print(f"Welcome {name}, to Game of Guessing .....")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'naveen',
         'ayushi', 'shweta', 'shraddha', 'prathamesh']  # list of words

actual_word = random.choice(words)
print(f"Hey I know it's cheating but here the actual word: {actual_word}")

print("Guess the word.....")

chances = 12
guesses = ''

while chances > 0:
    failed = 0
    for char in actual_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("You won!!")
        print(f"The word is: {actual_word}")
        break

    print()
    guess = input("Guess the the characters: ")
    guesses += guess

    if guess not in actual_word:
        chances -= 1
        print("wrong!!")
        print(f"number of chances left: {chances}")

    if chances == 0:
        print("You loose!!")















