# The following iterative sequence is defined for the set of positive integers:
#
# n ? n/2 (n is even)
# n ? 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def calculate_term(n):
    if n % 2 == 0:
	    return n / 2
    else:
	    return (3 * n) + 1
		
def calculate_chain_length(n):
    len = 1
    while n > 1:
	    n = calculate_term(n)
	    #print n
	    len += 1
    return len
	
import time
start = time.time()	
	
num = 999999
max = 0
while num > 0:
    l = calculate_chain_length(num)	
    if l > max:
	    max = l
	    print "num=", num, " len=", l
    num -= 1
		

print "Tiempo:", time.time() - start
