#Ryan Hayes
#1-100 Number Guessing Game
#Program has user guess a number between 1-100 and tells them if they are high or low until they get the number correct

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses
    num_guesses = 0

    while True:
        try:
            # Ask the user to guess the number
            user_guess = int(input("Guess the number between 1 and 100: "))
            num_guesses += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
            elif user_guess < secret_number:
                print("Too low, try again.")
            elif user_guess > secret_number:
                print("Too high, try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} "
                      f"in {num_guesses} guesses.")
                break  # Exit the loop when the user guesses correctly

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_the_number()
