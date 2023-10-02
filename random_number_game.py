import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        # Ask the player to guess the number
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

