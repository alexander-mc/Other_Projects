balance = 3926
annualInterestRate = 0.2

nbalance = balance
monthlyInterestRate = annualInterestRate/12
lowestPayment = 0

while nbalance > 0:
    nbalance = balance
    lowestPayment += 10
    for m in range (1,13):
        nbalance -= lowestPayment
        nbalance *= (monthlyInterestRate+1)

print 'Lowest Payment:',lowestPayment