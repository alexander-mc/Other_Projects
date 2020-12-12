# Python 2.17.13
# Project name: Guess the Number
# Project details: Find a number you are thinking about from 0-100
# Course: MITx 6.001x

# -----------------------------------

L = 0
H = 100
mid = (L + H)/2
r = 0

print 'Please think of a number between 0 and 100!'

while r != 'c':
    r = raw_input('Is your secret number ' + str(mid) + '? \nEnter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
 
    if r == 'h':
        H = mid
        mid = (L + H)/2
    elif r == 'l':
        L = mid
        mid = (L + H)/2
    elif r == 'c':
        break
    else:
        print 'Sorry, I did not understand your input.'
    
print 'Game over. Your secret number was: ' + str(mid)
