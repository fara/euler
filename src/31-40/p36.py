# The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

binary = lambda i, c = (lambda i, c: i and (c(i >> 1, c) + str(i & 1)) or ''): c(i, c) 

def is_pal(s):
    l = len(s)
    for i in range(l / 2):
	    if s[i] != s[l-1-i]:
		    return False
    return True

sum = 0
for i in range(1000000):
    if is_pal(str(i)) and is_pal(str(binary(i))):
        print i, binary(i)
        sum += i	
		
print sum
