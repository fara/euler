import operator
# A slightly efficient superset of primes.
def prime_list():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def prime_dec(n):
  d = {}
  for p in prime_list():
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
  
def count_divisors(n):
  d = prime_dec(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)


def divisors(n):
    c = 2
    for d in range(2, (n/2)+1):
        if n % d == 0:
            c = c + 1
    return c

t = 1
n = 1
while NumberOfDivisors(t) < 500:
    n = n + 1
    t = t + n
    
print t
 