from sys import exit

def gold_room():
	print """
	This room is full of gold. 
	How much do you want?
	"""
	next = raw_input("> ")
	#print type(next)
	
	if next.isdigit():
		how_much = int(next)
	else:
		dead("Man, learn to type a number")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print"""
	There is a bear here.
	The bear has a bunch of honey.
	The fat bear is in front of another door.
	How are you going to move the bear? 
	"""
	bear_move = False
	
	while True:
		next = raw_input("> ")
		#print next
	
		if next == "take honey":
			dead("The bear looks at you then slaps your face off")
		elif next == "taunt bear" and not bear_move:
			print "The bear moved from the door. You can go through if now."
			bear_move = True
		elif next == "taunt bear" and bear_move:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_move:
			gold_room()
		else:
			print "Sorry, that doesn't work with the fat bear."
		
def cthulhu_room():
	print"""
	Here you see the great evil Cthulhu.
	He, it, whatever stares at you and you go insane.
	Do you flee for your life or eat your head?
	"""
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty")
	else:
		cthulhu_room()

def dead(why):
	print why,"You dead!"
	exit(0)

def start():
	print """
	You are in a dark room,
	There is a door to your right and left
	Which one do you take?
	"""
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

#start()
gold_room()
