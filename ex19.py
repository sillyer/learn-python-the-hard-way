from sys import argv

def fish_and_frogs(mount_fish,mount_frogs):
	print "There are %d fish in the pond!" % mount_fish
	print "There are %d frogs in the pond!" % mount_frogs
	print "There are enough!\n"

print "1.give the number directly:"
fish_and_frogs(10,1)

print "2.use the var from our script:"
fish_num = 20
frogs_num = 2
fish_and_frogs(fish_num,frogs_num)

print "3.input the numbers:"
fish_num_input = int(raw_input("> the fish num:"))
frogs_num_input = int(raw_input("> the frogs num:"))
fish_and_frogs(fish_num_input,frogs_num_input)

print "4.do math inside:"
fish_and_frogs(10+20+30,1+2+3)

print "5.var and math combine:"
fish_and_frogs(fish_num+50,frogs_num+5)


