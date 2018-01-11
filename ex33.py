numbers = []

#while i<6 :
#	print "at the top i is %d" % i
#	numbers.append(i)
#	i = i+1
#	print "Number now: ", numbers
#	print "At the bottom i is %d" % i

def add_list(elem_range, num_list):
	i=0
	while(i<elem_range):
		print "add %d to %r" % (i,numbers)
		num_list.append(i)
		print "then the list is:", numbers
		i = i+1

add_list(6,numbers)
print "the numbers: "
for num in numbers:
	print num,
