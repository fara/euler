# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def proper_divisors(n):
    ret =[1]
    for i in range(2, n/2 + 1):
	    if n % i == 0:
		    ret.append(i)
    return ret

def d(n):
    sum = 0
    for p in proper_divisors(n):	
	    sum += p
    return sum

print proper_divisors(284)

print d(284)
	
sum = 0	
for n in range(1, 10000):
    a = n
    b = d(a)
    if d(b) == a and a != b:
	    print "a=", a, ", b=", b
	    sum += a + b

print sum / 2