# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.
# What is the 10001^(st) prime number?

def is_prime(n) :
    global primes
    for p in primes:
	    if n % p == 0:
		    return False	
    return True
	
import time
start = time.time()	
	
n = 1
primes = []
while True:
    n += 1
    if is_prime(n):
        primes.append(n)
        if len(primes) == 10001:
            break
print primes[-1]

print "Tiempo:", time.time() - start