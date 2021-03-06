# Pentagonal numbers are generated by the formula, P_(n)=n(3n-1)/2. The first ten 
# pentagonal numbers are:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# It can be seen that P_(4) + P_(7) = 22 + 70 = 92 = P_(8). However, their difference, 
# 70 - 22 = 48, is not pentagonal.
# Find the pair of pentagonal numbers, P_(j) and P_(k), for which their sum and 
# difference is pentagonal and D = |P_(k) - P_(j)| is minimised; what is the value of D?

pentagonals = []

def P(n):
	return n*(3*n-1)/2

def is_pent(n):
    global pentagonals
    return n in pentagonals
	
for i in range(1,3000):
	pentagonals.append(P(i))
	
for j in pentagonals:
	for k in pentagonals:
		if is_pent(j+k) and is_pent(k-j):
			print "!", j, k
			break
			

