# It was proposed by Christian Goldbach that every odd composite number 
# can be written as the sum of a prime and twice a square.

# 9 = 7 + 2x1^(2)
# 15 = 7 + 2x2^(2)
# 21 = 3 + 2x3^(2)
# 25 = 7 + 2x3^(2)
# 27 = 19 + 2x2^(2)
# 33 = 31 + 2x1^(2)

# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum 
# of a prime and twice a square?

import itertools
def erat2():
    # from Python Cookbook, 2nd Edition, recipe 18.10
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def is_prime(n):
    for p in erat2():
        if n == p: return True
        elif p*p > n: return True
        elif n%p == 0: return False
                    
def sum_of_prime_and_square(n):
    for p in erat2():
        for s in range(1, n - p):
            if n == p + 2 * s * s:
                return True
        if p > n:
            return False
          
import time
start = time.time()              
            
n = 1            
while n < 6000:
    if not is_prime(n):
        if not sum_of_prime_and_square(n):
            print "----", n
            break
    n += 2             
            
print "Tiempo:", time.time() - start            