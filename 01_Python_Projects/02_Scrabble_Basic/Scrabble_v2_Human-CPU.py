# Python 2.17.13
# Project name: Scrabble v2 (player vs computer)
# Project details: Earn points for creating as many words possible
#                  from a set of 7 letters. Earn more points than the computer!
# Course: MITx 6.001x

# -----------------------------------

from Scrabble_Basic_V1 import *
import time

def compChooseWord(hand, wordList, n):

    maxScore = 0    
    bestWord = None

    for word in wordList:
        lenWord = 0

        for letter in word:
            if letter not in hand:
                break
            else:
                lenWord += 1

        if lenWord == len(word) and isValidWord(word, hand, wordList):          
            scoreWord = 0
            scoreWord = getWordScore(word, n)        
            
            if scoreWord > maxScore:
                maxScore = scoreWord
                bestWord = word

    return bestWord

def compPlayHand(hand, wordList, n):

    totalScore = 0
        
    word = ""
    currentHand = hand

    while calculateHandlen(currentHand) > 0:
        print 'Current hand: ',
        displayHand(currentHand)
        word = compChooseWord(currentHand, wordList, n)
    
        if word != None:
            scoreWord = 0
            scoreWord = getWordScore(word, n)           
            totalScore += scoreWord
            print '\"'+str(word)+'\"' + ' earned '+str(scoreWord)+' points. Total: '+str(totalScore)+' points'
            currentHand = updateHand(currentHand, word)      
        else:
            break
    
    print 'Total score: '+str(totalScore)+' points.'

def playGame(wordList):

    n = HAND_SIZE
    a = 0
    
    loop1 = 1
    while loop1 > 0:
        input1 = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))

        if input1 == 'e':
            loop1 = 1
            break
        if input1 == 'r' and a == 0:
            print "You have not played a hand yet. Please play a new hand first!"
        elif input1 == 'r' or input1 == 'n':
            loop2 = 1
            while loop2 > 0:
                input2 = str(raw_input("Enter u to have yourself play, c to have the computer play: "))            
                if input1 == 'n':
                    if input2 == 'u':
                        a = dealHand(n).copy()    
                        playHand(a, wordList, n)
                        break
                    elif input2 == 'c':
                        a = dealHand(n).copy()                            
                        compPlayHand(a, wordList, n)
                        break
                    else:
                        print'Invalid command.'                                        
                elif input1 == 'r':           
                    if input2 == 'u': 
                        playHand(a, wordList, n)
                        break
                    elif input2 == 'c':
                        compPlayHand(a, wordList, n)
                        break
                    else:
                        print'Invalid command.' 
        else:
            print 'Invalid command.'

# Builds data structures used for entire session and play game

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

wordList = loadWords()
