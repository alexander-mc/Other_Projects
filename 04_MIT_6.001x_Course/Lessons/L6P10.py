animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

a = {'l': []}
b = {}

def biggest(aDict):
    count = 0
    key = ""
    
    if aDict == {}:
        return None
    
    for k in aDict:
        if len(aDict[k]) >= count:
            count = len(aDict[k])
            key = k
    return key
    
print biggest(b)