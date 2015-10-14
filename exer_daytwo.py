word_sequence = ['appa', 'bob', 'dud', 'gniing', 'eettimmocommittee', '10010001001', '10110001101', '10']

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
					seq.remove(item)

		return func(seq)

	return inner 


#Item 1. count number of unique letters that make up a word
@palindrome
def list_unique_letter_count(words):
	return [len(set(word)) for word in words]

def generate_repeating_letter_dict(word):
	dllist = {}
	temp = ''
	for letter in word:
		if len(temp)>0:
			if letter == temp[0]:
				temp += letter
			else:
				if len(temp)>1:
					if(temp in dllist.keys()):
						dllist[temp] += 1
					else:
						dllist[temp] = 1
				temp = letter
		else:
			temp = letter
	if len(temp) > 1:
		if(temp in dllist.keys()):
			dllist[temp] += 1
		else:
			dllist[temp] = 1
	return dllist

#Item 2: 
@palindrome
def list_double_letters(words):
	dllist = []
	for item in words:
		dlist = generate_repeating_letter_dict(item)
		if len(dlist.keys()) > 0:
			dllist.append(dlist)
	
	return dllist


print 'unique letters: ', list_unique_letter_count(word_sequence)
print 'double letters: ', list_double_letters(word_sequence)