# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p <= 1000, is the number of solutions maximised?

max_sol = 0
max_p = 0
for p in range(3, 1000):
    sides = []
    solutions = 0
    for a in range(1, p):
        for b in range(1, p - a):
            c = p - a - b
            if a*a + b*b == c*c:
                if not (a in sides or b in sides or c in sides):
                    sides.extend([a, b, c])
                    #print a, b, c
                    solutions += 1
    
    print solutions, " solutions for P =", p
    if solutions > max_sol:
        max_sol = solutions
        max_p = p
        
print " P =", max_p, " has ", max_sol, " solutions"