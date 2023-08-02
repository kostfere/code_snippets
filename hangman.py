# coding: utf-8

import random
hanged_stages=['''
------------
|         |         
|          O''','''


------------
|         | 
|          O 
|         / ''','''


------------
|         | 
|          O 
|         / |''','''

------------
|         | 
|          O 
|         / |
|          | ''','''


------------
|         |
|          O 
|         / |
|          |
|         /  
|
|            ''','''


------------
|         |
|          O 
|         / |
|          |
|         / | 
|
|            ''']

def word_exists(all_chars, word):
    # if all the letter required for making the word are present return true else false
    return all([c in all_chars for c in word])

def get_new_char_from_user(chars_till_now):
    while True:
        new_char=input("\n\nEnter your guess: ")
        new_char = new_char[0].lower() ## take the first character and make it lowercase
        if new_char in chars_till_now: ## check if the user has already selected this character
            print('You have already chosen this letter')
        elif new_char not in 'abcdefghijklmnopqrstuvwxyz0123456789': ## make sure it's  valid
            print('Your selection is invalid')
        else:
            return new_char

def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

words= ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']

## initialize parameters
random_choice =random.randint(0,len(words)-1)
word = words[random_choice]
nr_mistakes=0
chars_till_now=''
game_done = False
cnt=0

while True:
    if cnt==0:
        print("Let's play Hangman!!! You can make up to 5 mistakes")
        print(f"The word has {len(word)} characters: ")
        print("_"*len(word))
        cnt+=1
        
    new_char = get_new_char_from_user(chars_till_now)
    chars_till_now = chars_till_now+new_char

    if new_char in word: ## in case of correct guess
        print(f"The letter '{new_char}' is in the word.")
        print(''.join(c if c in chars_till_now else '_' for c in word))
        if word_exists(chars_till_now,word):
            print("Congats, you found the word!!!")
            game_done = True

    else: ## in case of incorrect guess
        print(f"The letter '{new_char}' is not in the word.")
        print(hanged_stages[nr_mistakes])
        nr_mistakes += 1
        print(''.join(c if c in chars_till_now else '_' for c in word)) 
        if nr_mistakes==6:
            print("You failed!!! The word was:", word)
            game_done = True
            
    if game_done:
        if nr_mistakes<=2: ## high score is defined as 2 mistakes or less
            if nr_mistakes==0:
                print('Wow you achieved high score, no wrong guesses!!')
            else:
                print(f'Wow you achieved high score, only {nr_mistakes} wrong guesses!!')
        if play_again():
            ## in case of new game re-initialize parameters
            random_choice =random.randint(0,len(words)-1)
            word = words[random_choice]
            nr_mistakes=0
            chars_till_now=''
            game_done = False
            cnt=0
        else:
            break
