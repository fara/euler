# The number 3797 has an interesting property. Being prime itself, it is possible to 
# continuously remove digits from left to right, and remain prime at each stage: 
# 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

primes = [2,3,5,7]
def is_prime(n) :
    if n == 1:
        return False
    global primes
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
    primes.append(n)    
    return True

# superset of primes
def prime_list():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
    
def all_primes(str_num):
    if str_num[0] in "4689":
        return False
    if str_num[-1:] in "4689":
        return False
    for i in range(1, len(str_num) + 1):
        if not is_prime(int(str_num[:i])):
            return False
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
        
    return True     


sum = 0
cant = 1    
for n in prime_list():
    #print n
    if n in [2,3,5,7]:
        continue
    if is_prime(n):
        if all_primes(str(n)):
            print str(cant) + " : " + str(n)
            sum += n
            cant += 1
    if cant == 12:
        break

print sum    