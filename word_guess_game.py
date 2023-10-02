import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon", "pineapple", "blueberry"]

# Function to choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Function to display the masked word with underscores for unrevealed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the game
def play_game():
    secret_word = choose_word(word_list)
    guessed_letters = []
    attempts = 6  # You can change the number of attempts here

    print("Welcome to the Word Guessing Game!")
    print(f"I'm thinking of a word with {len(secret_word)} letters.")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        guess = input("Guess a letter or the whole word: ").lower()

        if guess == secret_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif len(guess) == 1 and guess.isalpha():
            guessed_letters.append(guess)
            if guess in secret_word:
                print("Good guess!")
                if display_word(secret_word, guessed_letters) == secret_word:
                    print(f"Congratulations! You guessed the word: {secret_word}")
                    break
            else:
                print("Try again. This letter is not in the word.")
                attempts -= 1
        else:
            print("Invalid input. Please enter a single letter or the whole word.")

    else:
        print(f"Sorry, you're out of attempts. The word was: {secret_word}")

# Start the game
play_game()
