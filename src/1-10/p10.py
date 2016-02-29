# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(n) :
    global primes
    for p in primes:
	    if n % p == 0:
		    return False	
    return True
	
import time
start = time.time()	
	
n = 5
primes = [2, 3]
sum = 5
i = 1
while True:

    n = 6*i - 1		
    if n >= 2000000:
        break
    if is_prime(n):
        primes.append(n)	
        sum += n			

    n = 6*i + 1		
    if n >= 2000000:
        break
    if is_prime(n):
        primes.append(n)	
        sum += n			
		
    i += 1

print sum

print "Tiempo:", time.time() - start