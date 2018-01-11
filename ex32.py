numbers = [1,2,3,4,5]
fruits = ['apple','orange','banana','strawburry','lemon']
change = ['apple',1,'orange',2,'banana',4]

for count in numbers:
	print "the number is %d" % count

for fruit in fruits:
	print "the fruit is %s" % fruit

for i in change:
	print "the output is %r" % i

element = []

for a in range(0,6):
	print "Adding %r to the list." % a
	element.append(a)

for elem in element:
	print "Element is %r" % elem
