import  logging
logging.basicConfig(level	=logging.DEBUG)
# generating fibonacil numbers

fibNumbers = [1, 2]

while fibNumbers[-1] < 4000000:
	fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])

del fibNumbers [-1]

logging.debug(fibNumbers)

# find all even numbers

evenFibNumbers = []
for fibNumber in fibNumbers:
	if fibNumber % 2 == 0:
		evenFibNumbers.append(fibNumber)

logging.debug(evenFibNumbers)

# sum all of even numbers
totalSum = 0
for number in evenFibNumbers:
	totalSum += number

	print (totalSum)