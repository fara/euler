# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# 
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

def cant_c_primes(n):

    i = 0
    for p in erat2():
        if p > n:
            break
        s = p
        cant = 1
        primes = [p]
        for pp in erat2():
            if pp > n:
                break
            if pp > p:
                s += pp
                cant += 1
                primes.append(pp)
                if s == n:
                    print n, primes
                    return cant
            
                
    return 0
    
        
print cant_c_primes(41)        
        
max = 0
max_p = 0
for p in erat2():
    c = cant_c_primes(p)
    if c > max:
        max = c
        max_p = p
    if p > 1000:
        break
             
print max_p, max                