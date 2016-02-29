# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

def is_pandigital(n):
    for i in range(1, len(n)+1):
        if not str(i) in n:
            return False
    return True
         
    #return "1" in n and "2" in n and "3" in n and "4" in n and "5" in n and "6" in n and "7" in n and "8" in n and "9" in n

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
        
def prime_list():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
    
#print is_pandigital("123")    
 
n = 0   
n = 999999999

     
while n > 1:
    if is_pandigital(str(n)):
        #print n
        if is_prime(n): 
            print "----", n
            break
    n -= 2        