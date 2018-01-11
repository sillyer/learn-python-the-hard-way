t_cat = "\tI'm t in."
p_cat = "I'm split \non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print t_cat
print p_cat
print backslash_cat
print fat_cat

for i in ["/","-","|","\\","|"]:
	print "%r\n" % i,
