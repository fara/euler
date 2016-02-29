# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^(2) + b^(2) = c^(2)
# 
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

i = 1
while True:
    c = i
    for a in range(1, c):
	    for b in range(1, a):
	        if (a * a) + (b * b) == c * c and a + b + c == 1000:
			    print a, b, c, a * b * c
			    break
    i += 1