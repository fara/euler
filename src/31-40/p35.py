# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

def prime_list(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]


def is_circular_prime(p):
    global primes
    s = str(p)
    for i in range(len(s)-1):
        rot = int(s[i+1:]+s[:i+1])
        if not rot in primes:
            return False
    return True 

primes = prime_list(100)
count = 0
    
for p in primes:   
    if is_circular_prime(p):
        count += 1
        
print count