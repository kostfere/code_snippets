# coding: utf-8
import random

MAX_MISTAKES = 5
ALLOWED_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz0123456789'
WORDS = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']

def play_game():
    word = get_random_word()
    guessed_chars = set()
    mistakes = 0

    print(f"Let's play Hangman! You can make up to {MAX_MISTAKES} mistakes.")
    print(f"The word has {len(word)} characters: {'_' * len(word)}")

    while mistakes <= MAX_MISTAKES:
        print(f"\nGuessed letters: {', '.join(sorted(guessed_chars))}")
        print(f"Mistakes remaining: {MAX_MISTAKES - mistakes}")
        guess = get_user_guess(guessed_chars)
        guessed_chars.add(guess)

        if guess in word:
            revealed_word = reveal_word(word, guessed_chars)
            print(f"The letter '{guess}' is in the word: {revealed_word}")
            if '_' not in revealed_word:
                print("Congrats, you found the word!")
                return
        else:
            mistakes += 1
            print(f"The letter '{guess}' is not in the word. Number of mistakes: {mistakes}")

    print(f"You failed! The word was: {word}")

def get_random_word():
    return random.choice(WORDS)

def get_user_guess(guessed_chars):
    while True:
        guess = input("\n\nEnter your guess: ")[0].lower()
        if guess in guessed_chars:
            print('You have already chosen this letter.')
        elif guess not in ALLOWED_CHARACTERS:
            print('Your selection is invalid.')
        else:
            return guess

def reveal_word(word, guessed_chars):
    return ''.join(c if c in guessed_chars else '_' for c in word)

def play_again():
    return input('Do you want to play again? (yes or no) ').lower().startswith('y')

def main():
    while True:
        play_game()
        if not play_again():
            break

if __name__ == '__main__':
    main()
