def genPrimes():
    
    primes = []
    output = 1
    
    while True:
        output +=1
        for a in primes:
            if output%a == 0:
                break
        else:
            primes.append(output)
            yield output

foo = genPrimes()

for n in foo:
    print n