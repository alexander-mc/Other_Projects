balance = 320000
annualInterestRate = .2

monthlyInterestRate = annualInterestRate/12
lBound = balance/12
uBound = (balance*((1+monthlyInterestRate)**12))/12

nbalance = balance + 1

while (nbalance - balance) > .01 or (nbalance - balance) < 0:
    nbalance = balance
    for i in range(1,13):
        mid = (lBound + uBound)/2           
        nbalance -= mid
        nbalance *= (monthlyInterestRate + 1)
    if nbalance > 0:
        lBound = mid
    else:
        if nbalance >= -.01:
            break
        else:
            uBound = mid

print 'Lowest Payment:', float("{0:.2f}".format(mid))