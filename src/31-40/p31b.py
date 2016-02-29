# In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:
#     1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
# It is possible to make L2 in the following way:
#     1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can L2 be made using any number of coins?

count = 1
print range(2+1)

for p in range(200+1):
	a = p
	if p == 200:
		count += 1
	print p
	for p2 in range(100+1):
		b = a + (p2 * 2)
		if b == 200:
			count += 1
		if b > 200:
			break
		for p5 in range(40+1):
			c = b + (p5 * 5)
			if c == 200:
				count += 1
			if c > 200:
				break
			for p10 in range(20+1):
				d = c + (p10 * 10)
				if d == 200:
					count += 1
				if d > 200:
					break
				for p20 in range(10+1):
					e = d + (p20 * 20)
					if e == 200:
						count += 1
					if e > 200:
						break
					for p50 in range(4+1):
						f = e + (p50 * 50)
						if f == 200:
							count += 1
						if f > 200:
							break
						for p100 in range(2+1):
							g = f + (p100 * 100)
							if g == 200:
								count += 1

print count