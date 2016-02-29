# -*- coding: utf-8 -*-

# Considering quadratics of the form:

#    n^2 + an + b, where |a| < 1000 and |b| < 1000

#    where |n| is the modulus/absolute value of n
#    e.g. |11| = 11 and |−4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.
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

def is_prime(N):
    for p in erat2():
        if N == p: return True
        elif p*p > N: return True
        elif N%p == 0: return False        
        
max = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while is_prime(abs((n*n) + (a*n) + b)):
            n = n + 1
        if n >= max:
            max = n
            print a, b, n, (a*b)         