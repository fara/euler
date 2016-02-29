# n! means n x (n - 1) x ... x 3 x 2 x 1
# Find the sum of the digits in the number 100!

def factorial(n):
    if n == 1:
	    return 1
    return n * factorial(n-1)
	
num = factorial(100)
tot = 0
for d in str(num):
    tot += int(d)	
print tot
