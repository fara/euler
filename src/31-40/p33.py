# The fraction ^(49)/_(98) is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that ^(49)/_(98) = ^(4)/_(8), which 
# is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

def value(fraction):
    if fraction[1] == 0:
         return 0
    return fraction[0] / float(fraction[1])

def simplify(fraction):
    
    num = str(fraction[0])
    den = str(fraction[1])
    # discard trivial
    if num[-1:] == "0" and den[-1:] == "0":
        return fraction
    for d in num:
        if d in den:
            num = num.replace(d, "", 1)
            den = den.replace(d, "", 1)
    if len(num) == 0 or len(den) == 0:
        return fraction
    else:
        return (int(num), int(den))

def list_four_curious_fractions():
    for i in range(10, 100):
        for j in range(i+1, 100):
            frac = (i,j)
            s_frac = simplify(frac)
            if frac != s_frac and value(frac) == value(s_frac):
                yield frac

def multiply(a, b):
    return (a[0] * b[0], a[1] * b[1])

def really_simplify(f):    
    for i in range(2, f[0]+1):
        if f[0] % i == 0 and f[1] % i == 0:
            return really_simplify((f[0]/i, f[1]/i))
    return f
    
m = (1,1)
for f in list_four_curious_fractions():
    m = multiply(m, simplify(f))
     
print really_simplify(m)
#print simplify((30,50))