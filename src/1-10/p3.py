#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

num = 0
while True:
    num = num + 1
    if 600851475143 % num == 0:
	    print num
    if num > 600851475143:
	    break
print "listo"
	