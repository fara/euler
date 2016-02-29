# The 5-digit number, 16807=7^(5), is also a fifth power. Similarly, the 9-digit number, 134217728=8^(9), is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

count = 0
for n in range(1, 25):
    i = 1
    p = i ** n
    print n
    while p < 10**n:
	    if p >= 10**(n-1):
	        count += 1
	        print p, "=", i, "^", n
	    i += 1
	    p = i ** n
		
print count