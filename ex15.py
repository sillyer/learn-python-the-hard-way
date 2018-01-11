from sys import argv

script, file_path = argv

txt = open(file_path)

print "Here's your file %r:" % file_path
print txt.read()

print "Type the file name again:"
file_path = raw_input("> ")

txt = open(file_path)

print txt.read()
