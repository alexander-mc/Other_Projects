# Python 2.17.13
# Project name: Substring exercise
# Project details: Find the longest substring of unique letters
# Course: MITx 6.001x

# -----------------------------------

s = raw_input('Type a string of random letters and then press Enter: \n\
')
a = 0

string1 = s[a]
string2 = ''

for i in range (0,len(s)-1):
    while s[a] <= s[a+1]:
        string1 = string1 + s[a+1]
        a += 1
        if a >= (len(s) - 1):
            break
    a += 1
    if len(string1) > len(string2):
        string2 = string1
    if a >= (len(s)-1):
        break
    string1 = s[a]

print 'The longest substring of unique letters in alphabetical order is:',string2

