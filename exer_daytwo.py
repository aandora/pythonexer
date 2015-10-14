word_sequence = ['appa', 'bob', 'dud', 'gniing', 'eettimmocommittee']
dletters = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

#Item 3. Palindrome checker
def palindrome(func):
	def inner(seq):
		for item in seq:
			if not isinstance(item, str):
				return 'not all items are string'
			else:
				med = (len(item)/2)
				first_half = ''
				if len(item)%2==0:
					first_half = item[0:med]
				else:
					first_half = item[0:med+1]
				second_half = item[med:len(item)]
				second_half = second_half[::-1]
				if(first_half!=second_half):
					return 'not all items are palindrome'

		return func(seq)

	return inner 


#Item 1. count number of unique letters that make up a word
@palindrome
def list_unique_letter_count(words):
	return [len(set(word)) for word in words]

def generate_double_letter_dict(word):
	dllist = {}
	for l in dletters:
		c = word.count(l)
		if(c>0):
			dllist[l]=c
	return dllist

#Item 2: 
@palindrome
def list_double_letters(words):
	return [generate_double_letter_dict(item) for item in words]


print 'unique letters: ', list_unique_letter_count(word_sequence)
print 'double letters: ', list_double_letters(word_sequence)