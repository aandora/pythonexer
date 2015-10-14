set = xrange(0, 20)

def fibonacci(n):
	prev1 = 1
	prev2 = 0
	for i in n:
		if(i == 0):
			yield prev2
		elif(i==1):
			yield prev1
		else:
			sum = prev1 + prev2
			prev2 = prev1
			prev1 = sum
			yield sum

for x in fibonacci(set):
	print x