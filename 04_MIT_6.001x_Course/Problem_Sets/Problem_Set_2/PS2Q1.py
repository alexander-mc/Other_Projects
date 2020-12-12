balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

monthlyInterestRate = annualInterestRate/12
totalPaid = 0

for m in range(1,13):
    print 'Month:',m
    print 'Minimum monthly payment:', float("{0:.2f}".format(balance*monthlyPaymentRate))
    totalPaid += balance*monthlyPaymentRate
    balance -= balance*monthlyPaymentRate
    balance *= monthlyInterestRate+1
    print 'Remaining balance:', float("{0:.2f}".format(balance))

print 'Total paid:', float("{0:.2f}".format(totalPaid))
print 'Remaining balance:', float("{0:.2f}".format(balance))