# Take the number 192 and multiply it by each of 1, 2, and 3:

#     192 x 1 = 192
#     192 x 2 = 384
#     192 x 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

def is_pandigital(n):
    if len(n) != 9:
        return False
    return "1" in n and "2" in n and "3" in n and "4" in n and "5" in n and "6" in n and "7" in n and "8" in n and "9" in n


import time
start = time.time()    


max = 0
i = 0
while i < 99999:
    num = str(i)
    mult = 2
    while len(num) < 9:
        num += str(i * mult)
        mult += 1
    if is_pandigital(num) and int(num) > max:
        max = int(num)
        print "i=", i, " num=", num
    i += 1

print "Tiempo:", time.time() - start


