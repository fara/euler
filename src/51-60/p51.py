# By replacing the 1^(st) digit of *3, it turns out that six of the nine possible values: 
# 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3^(rd) and 4^(th) digits of 56**3 with the same digit, 
# this 5-digit number is the first example having seven primes among the ten 
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, 
# and 56993. Consequently 56003, being the first member of this family, is the 
# smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily 
# adjacent digits) with the same digit, is part of an eight prime value family.
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
        
def replace(orig, positions, nr):
    n = str(orig)
    ret = ""
    for i in range(len(n)):
        if i in positions:
            ret += str(nr)
        else:
            ret += n[i]
    return int(ret)

print replace(12345, [2,3], 9)        

#def get_candidates(p):
    

for p in erat2():
    if p > 56003:
        candidates = get_cantidates(p)
        if candidates > 8:
            for c in candidates:
                if is_prime(c):
                    return p