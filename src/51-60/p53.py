# How many, not necessarily distinct, values of  
# ^(n)C_(r), for 1 <= n <= 100, are greater than one-million?

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

cant = 0
for n in range(1, 101):
    for r in range(1, n):
        if C(n, r) > 1000000:
            cant += 1

print cant