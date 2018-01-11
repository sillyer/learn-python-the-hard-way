test_L = [1,1,3,5,'a','a','ab','abc','bc','abcd']
add_L = ['a1','a2','a3']

def print_list(L_name):
	for i in L_name:
		print i,
	print "\n"				

test_L.append('add+')

num_1 = test_L.count(1)
print "number of 1 : %d; " % num_1

char_a = test_L.count('a')
print "number of char 'a' : %d; " % char_a

char_add = test_L.count('add+')
print "number of char 'add+' : %d" % char_add

test_L.extend(add_L)

print test_L.index('a1')

test_L.insert(1,'insert1')
print test_L.index('insert1')

print "\n---the pop([index]) method return item-----"
print test_L.pop(1)

print "\n---remove(value) method---"
print "orignal the test_L output:",
for i in test_L:
	print i,
print "\n"
test_L.remove('add+')
test_L.remove(5)
print "after remove, the test_L is:",
for i in test_L:
	print i,
print "\n"


print "\n---the sort method test---"
test_L.sort()
print "after sort, the test_L is:"
print_list(test_L)
