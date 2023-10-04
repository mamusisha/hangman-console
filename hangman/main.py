import random
from words import words
import string


# choose valid(not contains '-' or ' ') word from the list
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()    

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #set of word's letters
    alphabet = set(string.ascii_uppercase)  #set of uppercase letters
    used_letters = set()  #set to track used letters

    lives = 9

    #while word is guessed
    while len(word_letters) > 0 and lives > 0:   
        #giving current information
        print(f'You have {lives} lives left')
        print('You used this letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        

        #getting a letter
        user_letter = input('\nguess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:    #correct
                word_letters.remove(user_letter)
                print("Letter is in the word, GG!")
            else:   #incorrect
                lives = lives - 1
                print('Letter is not in the word, OPPS!') 
        elif user_letter in used_letters:
            print("You used that letter")
        else:
            print("NOT VALID!")    

    #after you win or you die
    if lives == 0:
        print(f"You Died, SORRY! word was {word}")
    else:    
        print(f'You guessed the word: {word}, CONGRATS!')

hangman() #let's play!