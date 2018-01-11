from sys import argv

first=raw_input("first arg: ")
second=raw_input("second arg: ")
third=raw_input("third arg: ")
script, first, second, third = argv


print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
