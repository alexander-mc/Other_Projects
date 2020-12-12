# Python 2.17.13
# Project name: Hangman!
# Project details: Guess the word in 8 tries
# Course: MITx 6.001x

# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "/Users/Alexander/Documents/Coding/0_GitHub_Portfolio/Other_Projects/01_Python_Projects/01_Hangman_Game/words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded. \n\
    "
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    stringAns = secretWord
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            stringAns = stringAns.replace(secretWord[i],'_ ')
    return stringAns

def getAvailableLetters(lettersGuessed):
    import string
    alphab = string.ascii_lowercase
    lLeft = ""
    for i in alphab:
        if i not in lettersGuessed:
            lLeft = lLeft + i
    return lLeft
    
def hangman(secretWord):
    numGuesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangman! \n\
    I am thinking of a word that is '+str(len(secretWord))+' letters long. \n\
    '
    while numGuesses > 0:
        print 'You have '+str(numGuesses)+' guesses left. \n\
        Available letters: '+ getAvailableLetters(lettersGuessed)
        g = raw_input('Please guess a letter:')
        g = g.lower()
        if g not in getAvailableLetters(lettersGuessed):
            print 'Oops! You\'ve already guessed that letter: '+getGuessedWord(secretWord,lettersGuessed)+'\n\
            '
        else:
            lettersGuessed.append(g)          
            if g in secretWord:
                print 'Good guess: '+getGuessedWord(secretWord,lettersGuessed)+'\n\
                '
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print 'Congratulations, you won!'
                    break
            else:
                numGuesses -= 1
                print 'Oops! That letter is not in my word: '+getGuessedWord(secretWord,lettersGuessed)+'\n\
                '
    if numGuesses == 0:
        print 'Sorry, you ran out of guesses. The word was '+str(secretWord)+'.'

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
