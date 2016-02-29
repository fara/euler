# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 
# 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting 
# this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
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
        
def four_digit_seq():
    for i in range(1000, 10000):
        for n in range(1, (10000-i)/2):
            yield (i, i + n, i + n + n)  
            
def prime_seq(seq):
    return is_prime(seq[0]) and is_prime(seq[1]) and is_prime(seq[2])
            
def perm(seq):
    a = str(seq[0])
    b = str(seq[1])
    c = str(seq[2])
    for d in a:
        a = a.replace(d, "", 1)
        b = b.replace(d, "", 1)
        c = c.replace(d, "", 1)
    return len(a) == 0 and len(b) == 0 and len(c) == 0            
           
print perm((1471, 4441, 7411))

for seq in four_digit_seq():
    if prime_seq(seq):
        if perm(seq):
            print seq                        
