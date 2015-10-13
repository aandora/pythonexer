def half_triangle(number):
	triangle = ""
	for i in xrange(1, number+1):
		for j in xrange(0, i):
			triangle += "1"
		triangle += "\n"

	print triangle

print "\nHALF TRIANGLE\n"
half_triangle(5)

def pyramid_a(number):
	triangle = ""
	width = number*4+1;
	median = number*2;
	for i in xrange(0, number):
		for j in xrange(0, width):
			diff = abs(j-median)
			if(diff>2*i):
				triangle += " "
			else:
				if(diff%2==0):
					triangle += "1"
				else:
					triangle += " "
		triangle += "\n"

	print triangle

print "\nPYRAMID A\n"
pyramid_a(5)

def pyramid_b(number):
	triangle = ""
	width = number*2-1;
	median = number - 1;
	for i in xrange(0, number):
		for j in xrange(0, width):
			diff = abs(j-median)
			if(diff>i):
				triangle += " "
			else:
				if(diff%2 == i%2):
					triangle += "1"
				else:
					triangle += " "

		triangle += "\n"

	print triangle

print "\nPYRAMID B\n"
pyramid_b(5)