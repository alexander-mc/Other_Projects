def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    z = min(a,b)
    
    while z > 0:
        if a%z == 0 and b%z == 0:
            return z
            break
        z -= 1
    
    if z == 0:
        return z ==1
        
print gcdIter(12, 5)