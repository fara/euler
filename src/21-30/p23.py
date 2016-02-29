# A perfect number is a number for which the sum of its proper divisors is 
# exactly equal to the number. For example, the sum of the proper divisors 
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
# number.
#
# A number n is called deficient if the sum of its proper divisors is less 
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
# smallest number that can be written as the sum of two abundant numbers is 
# 24. By mathematical analysis, it can be shown that all integers greater 
# than 28123 can be written as the sum of two abundant numbers. However, 
# this upper limit cannot be reduced any further by analysis even though it 
# is known that the greatest number that cannot be expressed as the sum of 
# two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the 
# sum of two abundant numbers.

def divisors(n):
    yield 1
    for d in range(2, (n/2)+1):
        if n % d == 0:
            yield d    

abundant_nums = {}
def is_abundant(n):
    global abundant_nums
    if not n in abundant_nums:
        sum = 0
        for i in divisors(n):
            sum += i
        abundant_nums[n] =  sum > n
    return abundant_nums[n]

def cannot_be_sum_of_abundant_nums(n):
    for i in range(12, n - 11):
        if is_abundant(i) and is_abundant(n - i):
            return False
    return True

import time
start = time.time()    

sum = 0
for n in range(1, 28123):#28123):
    if cannot_be_sum_of_abundant_nums(n):
        sum += n

print sum

print "Tiempo:", time.time() - start