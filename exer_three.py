#Item 3
# given a roman numeral r, convert it to decimal

numval = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

r = "MCMXCIX"

numlist = [numval[x] for x in r]

num = 0;
for index, i in enumerate(numlist):
	try:
		if(numlist[index+1]>i):
			num -= i
		else:
			num += i
	except IndexError:
		num += i

print r, 'is equal to', num;