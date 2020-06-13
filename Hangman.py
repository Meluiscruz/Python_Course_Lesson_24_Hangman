# -*- coding: utf-8 -*-

import random           #Import random pack.
			#When a Var is in Capital letters, it is a constant. IMAGES is a list of ASCII art images
IMAGES = ['''           
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        |
    =========''']

WORDS = [                      #When a Var is in Capital letters, it is a constant. WORDS is a list of some spanish words.
    'oruga',
    'agente',
    'carpintero',
    'lámpara',
    'antorcha',
    'veneno',
    'capricornio',
    'escopeta',
    'hartazgo',
    'esfuerzo',
    'compilador'
    'proxeneta'
    'acuñar'
    'español'
    'exégeta'
    'hereje'
    'libélula'
    'numismática'
    'tejocote'
]

def random_word():                               #This function takes a random word from the list WORDS.
    idx = random.randint(0, len(WORDS) - 1)      #Remenber: We count from 0 to n-1. The feature randint returns a random integer between 2 values.
    return WORDS[idx]                            #Return the random word.

def display_board(hidden_word, tries):          #This function display the sequence from IMAGES.
    print(IMAGES[tries])                        #As the game runs, the var tries is the index that describes the game progess.
    print('')
    print(hidden_word)                          #The var hidden_word is dependent on the lenght of random_word (see line 99)
    print('--- * --- * --- * --- * --- * --- * ---')        #Image Separator

def run():
    word = random_word()                        #word is dependent on random_word() function.
    hidden_word = ['_']*len(word)               #See line 94.
    tries = 0                                   #When the game begins, the number of tries is 0.

    while True:                                                 #Infinite loop
        display_board(hidden_word, tries)                       #Displaying the right image depends by the number of tries.
        current_letter = str(input('Please, type a letter: '))  #In each attempt, the code asks the user typing any char.

        letter_indexes = []                                     #Initialize a void list of indexes

        for idx in range(len(word)):                            #Sweep the random word
            if word[idx] == current_letter:                     #If the swept letter is tye typed letter
               letter_indexes.append(idx)                       #Add idx to the end of the list letter_indexes.
        
        if len(letter_indexes) == 0:                            #If the lenght of letter_indexes is 0
            tries += 1                                          #Add and attempt

            if tries == 7:                                      #If the user runs out the available attempts.
                display_board(hidden_word,tries)                #Display the last image
                print('')
                print('You lose! The correct answer was {}'.format(word))       #Notify the user that they have lost.
                break                                           #Break the infinite while loop.
        else:                                                   #Else they still have any chance to win...  
            for idx in letter_indexes:                          #Sweep the letter_indexes list
                hidden_word[idx] = current_letter               #Assign the current_letter (typed by the user, see line 104) tho the idx-th element of hidden_word
             
            letter_indexes = []                                 #reset the list letter_indexes, ready for the next iteration.
        try:
            hidden_word.index('_')                              #Are there any void space ('_') in hidden_word list? Yes (line 102) / No (line 127)
        except ValueError:                                      #Catch the error, this is the right signal that the user have won!
            print('')
            print('Congratulations! You win. The word is: {}'.format(word))       #Notify the user that they have won.
            break                                               #Break the infinite while loop.

if __name__ == '__main__':
   print('W E L L C O M E  T O  H A N G M A N ... (S P A N I S H  E D I T I O N)')
   run()