#ITEM 2
#given a string s rewrite s so that no words have repeating letters. order must be retained

s = "door broom mice"

s2 = s.split()

s3 = " ".join([''.join(sorted(set(word), key=lambda x: word.index(x))) for word in s2]) #sorted set from stackoverflow

print s3
