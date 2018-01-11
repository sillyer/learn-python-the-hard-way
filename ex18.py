#This one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r,type %r, arg2: %r" % (arg1,type(arg1),arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)

#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no argument
def print_none():
	print "I got nonthin'."

print_two(18,"Shaw")
print_two_again("Zed","Shaw")
print_one("first")
print_none()
	
