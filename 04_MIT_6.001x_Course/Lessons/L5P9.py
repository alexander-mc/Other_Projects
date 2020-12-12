def semordnilap(str1, str2):
    
    if len(str1) != len(str2):
        return False
        
    elif (len(str1) == 1) or (len(str2) == 1):
        if str1 == str2:
            return True
        return False
    
    else:
        return (str1[0] == str2[-1])\
        and semordnilap(str1[1:],str2[:-1])
        
print semordnilap('hi','ih')