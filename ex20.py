from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(3)

def print_a_line(line_count,f):
	print line_count, f.readline()

current_file = open(input_file)

print "1.first let's print the whole file:\n"
print_all(current_file)

print "2.now, let's rewind,kind of like a tape."
rewind(current_file)

print "3.let's print three lines:"
print_a_line(1,current_file)
print_a_line(2,current_file)
print_a_line(3,current_file)
print_a_line(4,current_file)
