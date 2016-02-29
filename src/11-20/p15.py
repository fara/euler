# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

def factorial(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return n * factorial(n-1)

# PR40 = 40! / 20! . 20!

print factorial(40) / (factorial(20) * factorial(20)) 