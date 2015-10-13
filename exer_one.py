#ITEM 1
#given a string s, and a collection c, remove all elements of c in s using list comprehension

word = "Philadelphia"
c = ('a', 'e', 'i', 'o', 'u')

newlist = [x for x in word if x not in c]
newword = ''.join(newlist)

print newword
