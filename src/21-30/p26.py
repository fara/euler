# Find the value of d < 1000 for which ^(1)/_(d) contains 
# the longest recurring cycle in its decimal fraction part.

def longest_seq(s):
    
    ret = 1
    for l in range(1, len(s)/2) :
        i = len(s) / l
        if s[:l] == s[l:l*2]:
            ret = l
            break
        
    return ret
    
print longest_seq("121211")

max = 0
presicion = 100000
for d in range(1000, 2, -1):
    dec = (10 ** presicion) / d
    seq = longest_seq(str(dec))
    if seq > max :
        max = seq
        print d, max
        
