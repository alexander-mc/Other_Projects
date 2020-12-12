def isIn(char, aStr):
    
    if aStr == "" or (len(aStr) == 1 and char != aStr):
        return False
    else:    
        testchar = aStr[len(aStr)/2]
    
        if char == testchar:
            return True
        else:
            if char > testchar:
                aStr = aStr[(len(aStr)/2):]
                return isIn(char, aStr)
            elif char < testchar:
                aStr = aStr[:(len(aStr)/2)]
                return isIn(char, aStr)
        
print isIn ('z', 'abc')
