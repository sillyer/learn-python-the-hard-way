print 
"""
you enter a dark room with two doors. 
Do you go through door #1 or door #2?
"""

door = raw_input("input> ")

if door=="1":
	print 
	"""
	There's a giant bear bear here eating a cheese cake.
	What do you do?
	1. Take the cake.
	2. Scream at the bear.
	"""
	bear = raw_input("input> ")
	
	if bear=="1":
		print "The bear eats your face off. Good job!"
	elif bear=="2":
		print "The bear eats your legs off."
	else:
		print "Well, doing %s is probably better. Bear runs away"


