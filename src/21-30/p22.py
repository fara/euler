# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing 
# over five-thousand first names, begin by sorting it into alphabetical order. Then working 
# out the alphabetical value for each name, multiply this value by its alphabetical position 
# in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a 
# score of 938 x 53 = 49714.
# 
# What is the total of all the name scores in the file?

file = open("names.txt")

def alpha_value(name):
	sum = 0
	for ch in name:
		sum += ord(ch) - 64
	return sum
		
sum = 0
pos = 0
for line in file:
	names =  sorted(line.replace('"', '').split(','))
	for name in names:
	    pos += 1
	    sum += alpha_value(name) * pos

print sum		
	
