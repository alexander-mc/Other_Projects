# Python 2.17.13
# Project name: Scrabble v1 (self-mode)
# Project details: Earn points for creating as many words possible
#                  from a set of 7 letters
# Course: MITx 6.001x

# -----------------------------------

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "/Users/Alexander/Documents/Coding/0_Portfolio/Python/Scrabble_Basic/words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# (end of helper code)
# -----------------------------------

def getWordScore(word, n):
    
    score = 0
    
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              
    print                               

def dealHand(n):
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand

def updateHand(hand, word):
    newHand = hand.copy()

    for i in word:
        if i in newHand and newHand[i] != 0:
            newHand[i] = newHand.get(i, 0) - 1
    return newHand

def isValidWord(word, hand, wordList):
    wordFrequency = getFrequencyDict(word)
    
    for i in wordFrequency:
        if i not in hand or wordFrequency[i] > hand[i] or word not in wordList:
            return False
    return True

def calculateHandlen(hand):
    output = 0
    for i in hand:
        output += hand[i]
    return output

def playHand(hand, wordList, n):

    totalScore = 0
        
    word = ""
    currentHand = hand

    while calculateHandlen(currentHand) > 0:
        displayHand(currentHand)
        word = str(raw_input("Enter word, or a \".\" to indicate that you are finished:"))

        if word == ".":       
            break            
        else:
            if isValidWord(word, currentHand, wordList) == False:
                print "Invalid word, please try again. \n"
            else:
                print "\""+ word +"\""+ ' earned ' + str(getWordScore(word, n)) + ' points. Total '+str((totalScore+getWordScore(word,n)))  +' points.\n'
                totalScore += getWordScore(word,n)
                currentHand = updateHand(currentHand, word)                

    if word == '.':
        print 'Goodbye! Total score: '+str(totalScore)+' points.'
    else:
        print 'Ran out of letters. Total score: '+str(totalScore)+' points.'

def playGame(wordList):

    n = HAND_SIZE
    loop1 = 1
    
    while loop1 > 0:
        input1 = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")

        if input1 == 'n':
            a = dealHand(n).copy()
            playHand(a, wordList, n)
        elif input1 == 'r':
            try:
                playHand(a, wordList, n)
            except:
                print "You have not played a hand yet. Please play a new hand first!"
        elif input1 == 'e':
            loop1 = 0
            break
        else:
            print 'Invalid command.'   

# Builds data structures used for entire session and play game

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
