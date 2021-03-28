#Hangman Part 3
#Anthony Swift
#28/03/2021

import random


def pick_word(wordlist):

    '''
    Picks a word randomly from text file
    for the player to guess in the game
    '''
    
    #Open the file
    #Read through each line in the file
    #Strips the extra space at the end of each line
    #Append each line to the wordlist variable

    with open('words.txt','r') as f:
        line = f.readline().strip()
        while line:
            wordlist.append(line)
            line = f.readline().strip()
    f.close()

    #Randomly pick the word from the wordlist

    word = random.choice(wordlist)

    #Print the word to test
    print(word,"\n")

    return word

def guess_letter():

    #Ask player for guess
    #Input validation to check guess is valid (only a letter)
    

    valid_guesses = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    
    guess = input("\nGuess your letter: ").upper()
    while len(guess) != 1 or guess not in valid_guesses:
       guess = input("Guess your letter: ").upper() 
    letters = ""

    return guess, letters

def check_guess(guess, guessed, word, number_of_guesses):
    
    #Check if letter guessed is in the word and display if letter guessed is correct, incorrect or already guessed
    #Appends guessed letter to guessed variable if letter hasn't already been guessed
    

    if guess in guessed:
        print("Letter already guessed!","\n")
    elif guess in word:
        print("Correct!","\n")
        guessed.append(guess)
    else:
        print("Incorrect!","\n")
        number_of_guesses -= 1
        guessed.append(guess)

    return number_of_guesses

def display_letters(word, guessed, letters, guess):
                
    #Check letter guessed is in the word
    #Displays letters in word guessed correctly
    #Displays letters not guessed correctly as "-"

    for x in range(0,len(word)):
        if word[x] in guessed:
            letters += word[x]
        elif word[x] == guess:
            letters += word[x]
        else:
            letters += "-"
        
    print(letters)
    return letters

def display_number_of_guesses(number_of_guesses):
    
    #Displays number of guesses remaining
    #Includes picture art for the hangman

    if number_of_guesses == 0:
        print("""
               _____
              | _ _ |
              |  |  |
              | --- |
              |_____|
                 |
                 |
                /|/
                 |
                 |
                / /
                """)

    if number_of_guesses == 1:
        print("""
               _____
              | _ _ |
              |  |  |
              | --- |
              |_____|
                 |
                 |
                /|/
                 |
                 |
                / 
                """)
        
    if number_of_guesses == 2:
        print("""
               _____
              | _ _ |
              |  |  |
              | --- |
              |_____|
                 |
                 |
                /|/
                 |
                 |
                
                """)

    if number_of_guesses == 3:
        print("""
               _____
              | _ _ |
              |  |  |
              | --- |
              |_____|
                 |
                 |
                /|
                 |
                 |
                
                """)

    if number_of_guesses == 4:
        print("""
               _____
              | _ _ |
              |  |  |
              | --- |
              |_____|
                 |
                 |
                 |
                 |
                 |
                
                """)

    if number_of_guesses == 5:
        print("""
               _____
              | _ _ |
              |  |  |
              | --- |
              |_____|







                
                """)
        
    print("\nYou have", number_of_guesses, "guesses remaining")

def display_result(letters, word):

    #Lets the user know if they have won or lost
    #at the end of each game

    if letters == word:
        print("\nCongratulations, you have won!")
    else:
        print("\nGame over! You have run out of incorrect guesses")
    print("The correct word was", word)

def new_game(gameplay):

    #Ask player if they would like to play a new game at end of each game
    
    gameplay = input("\nWould you like to play a new game? (Y/N): ").upper()
    while gameplay != "Y" and gameplay != "N":
        gameplay = input("Would you like to play a new game? (Y/N): ").upper()  
    return gameplay
    
def main():

    gameplay = "Y"

    while gameplay == "Y":

        #List to store all words from text file
        wordlist = []

        #Stores the letters guessed correctly
        guessed = []

        #Set number of guesses
        number_of_guesses = 6

        #Letters variable to store letters guessed correctly
        letters = ""

        word = pick_word(wordlist)
    
        #Welcome player
        print("Welcome to Hangman!")
        print("-" * len(word))
    
        while letters != word and number_of_guesses > 0:
            guess, letters = guess_letter()
            number_of_guesses = check_guess(guess, guessed, word, number_of_guesses)
            letters = display_letters(word, guessed, letters, guess)
            display_number_of_guesses(number_of_guesses)
        display_result(letters, word)
        gameplay = new_game(gameplay)

main()
            








