import random

# Function to generate a random 4-digit number as the secret
def generate_secret_number():
    return str(random.randint(1000, 9999))

# Function to check the player's guess against the secret number
def check_guess(secret, guess):
    cows = 0
    bulls = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return bulls, cows

def main():
    print("Welcome to the Cows and Bulls Game!")
    print("I have selected a 4-digit number. Try to guess it.")

    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter your guess (4 digits): ")

        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        attempts += 1

        bulls, cows = check_guess(secret_number, guess)

        if bulls == 4:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")

if __name__ == "__main__":
    main()
