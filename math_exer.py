sequence=[1, 3, 5, 8, 7, 7, 6, 6, 3, 4]

def compute(s, **keywords):

	s.sort()
	l = len(s)
	
	mean = lambda seq: float(sum(seq)) / len(seq)

	def find_median():
		if(l%2==0):
			return (s[(l/2)]+s[(l/2)-1])/2.
		else:
			return s[(l/2)]

	def find_mode():
		keyset = set(s)
		valtable = dict((el,0) for el in keyset)
		for i in s:
			valtable[i] += 1

		highest = 0
		modelist = []
		for i in keyset:
			x = valtable[i]
			if(x>highest):
				modelist = [i]
				highest = x
			elif(x==highest):
				modelist.append(i)
		return modelist


	if(keywords['opt']=='mean'):
		return mean(s)
	elif(keywords['opt']=='median'):
		return find_median()
	elif(keywords['opt']=='mode'):
		return find_mode()
	elif(keywords['opt']=='sum'):
		return sum(s)
	elif(keywords['opt']=='min'):
		return s[0]
	elif(keywords['opt']=='max'):
		return s[l-1]


print 'for the sequence', sequence, ':'
print 'mean =', compute(sequence, opt='mean')
print 'median = ', compute(sequence, opt='median')
print 'mode = ', compute(sequence, opt='mode')
print 'sum = ', compute(sequence, opt='sum')
print 'min = ', compute(sequence, opt='min')
print 'max = ', compute(sequence, opt='max')

