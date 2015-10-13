import sys

def half_triangle(number):
	for i in xrange(1, number+1):
		for j in xrange(0, i):
			sys.stdout.write("1")
		print ""

print "\nHALF TRIANGLE\n"
half_triangle(5)

def pyramid_a(number):
	width = number*2-1;
	median = number - 1;
	for i in xrange(0, number):
		for j in xrange(0, width):
			if(abs(j-median)>i):
				sys.stdout.write(" ")
			else:
				sys.stdout.write("1")
		print ""

print "\nPYRAMID A\n"
pyramid_a(5)

def pyramid_b(number):
	width = number*2-1;
	median = number - 1;
	for i in xrange(0, number):
		for j in xrange(0, width):
			diff = abs(j-median)
			if(diff>i):
				sys.stdout.write(" ")
			else:
				if(diff%2 == i%2):
					sys.stdout.write("1")
				else:
					sys.stdout.write(" ")
		print ""

print "\nPYRAMID B\n"
pyramid_b(5)