import random

def get_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'typescript']
    return random.choice(words)

def display_word(word, guesses):
    display = ''
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += '_'
    return display

def play_game():
    word_to_guess = get_word()
    guessed_letters = []
    attempts = 6
    guessed_word = False

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word!")

    while attempts > 0 and not guessed_word:
        guess = input(f"Word: {display_word(word_to_guess, guessed_letters)}\nGuess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess not in word_to_guess:
                print(f"{guess} is not in the word. Try again.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                if '_' not in display_word(word_to_guess, guessed_letters):
                    guessed_word = True
        else:
            print("Invalid input. Please enter a single letter.")

        print(f"Attempts left: {attempts}")

    if guessed_word:
        print(f"Congratulations! You guessed the word: {word_to_guess}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

play_game()
