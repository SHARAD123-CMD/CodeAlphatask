import random
#this is a hangman program task given by code alpha

# List of words
words = ["python", "computer", "programming", "internship", "developer"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:
    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if complete word guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)