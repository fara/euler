F = 1
Fant = 1
n = 2
while True:
    t = F
    F = F + Fant
    Fant = t
    n += 1
    if len(str(F)) > 999:
	    break

print "n=", n
print "F=", F