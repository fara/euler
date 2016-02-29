# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12^(th) digit of the fractional part is 1.
# If d_(n) represents the n^(th) digit of the fractional part, find the value of the following expression.
# d_(1) x d_(10) x d_(100) x d_(1000) x d_(10000) x d_(100000) x d_(1000000
s = ""
for i in range(0, 1000000):
	s += str(i)

print s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]
print int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])