# 2520 is the smallest number that can be divided by each 
# of the numbers from 1 to 10 without any remainder.
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

n = 0
while True:
    n = n + 2520
    for i in range(1, 21):
        if not (n % i == 0):
            break
        if i == 20 :
            print n
            exit()
