import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
            attempts += 1
            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

guessing_game()