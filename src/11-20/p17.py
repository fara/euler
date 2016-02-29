# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

def uni(i):
    if i == 0:
	    return ""
    if i == 1:
	    return "one"
    if i == 2:
	    return "two"
    if i == 3:
	    return "three"
    if i == 4:
	    return "four"
    if i == 5:
	    return "five"
    if i == 6:
	    return "six"
    if i == 7:
	    return "seven"
    if i == 8:
	    return "eight"
    if i == 9:
	    return "nine"

def dec_uni(i):
    if i > 10 and i < 20:
	    return teen(i)	
    d = i / 10
    u = i % 10
    if d == 0:
	    return "" + uni(u)
    if d == 1:
	    return "ten" + uni(u)
    if d == 2:
	    return "twenty" + uni(u)
    if d == 3:
	    return "thirty" + uni(u)
    if d == 4:
	    return "forty" + uni(u)
    if d == 5:
	    return "fifty" + uni(u)
    if d == 6:
	    return "sixty" + uni(u)
    if d == 7:
	    return "seventy" + uni(u)
    if d == 8:
	    return "eighty" + uni(u)
    if d == 9:
	    return "ninety" + uni(u)		
	
def cen(i):
    c = i / 100
    h = "hundred"
    if i % 100 != 0:
	    h = "hundredand"
    if c == 0:
	    return ""
    else:
	    return uni(c) + h

def teen(i):
    if i == 11:
	    return "eleven"
    if i == 12:
	    return "twelve"
    if i == 13:
	    return "thirteen"
    if i == 14:
	    return "fourteen"
    if i == 15:
	    return "fifteen"
    if i == 16:
	    return "sixteen"
    if i == 17:
	    return "seventeen"
    if i == 18:
	    return "eighteen"
    if i == 19:
	    return "nineteen"		
		
count = 0
for i in range(1, 1000):

    str_num = cen(i) + dec_uni(i%100)	    
    count += len(str_num)
    print str_num

print count + len("onethousand")
