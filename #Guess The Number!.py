#Guess The Number!

import random

number = random.randint(1, 10)

print("Welcome to Guess The Number!")
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break

    