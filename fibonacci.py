def fibonaccil(n):
	if n == 1 or n == 2:
		return 1

	return fibonaccil(n-1) + fibonaccil(n-2)

# anotther function for fibonaccil
def fibonaccil2(n):
	a,b = 1,1
	for i in range(n-1):
		a, b = b, a+b
	return a


# for i in range(1,11):
# 	print (fibonaccil2(i))


# function for fibonaccil usig generater
def fibonaccil3():
	a,b = 1,1
	while True:
		yield a
		a,b = b, a+b

n = 0
for i in fibonaccil3():
	if n >= 10:
		break;
		print (i)
		n += 1