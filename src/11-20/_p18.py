# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.

tri = [[3],[7, 4],[2, 4, 6],[8, 5, 9, 3]]

sum = 0
m = 20
for col in range(4):
	for row in range(col+1):
		sum += tri[col][row]
	if sum > max:
		m = sum
	sum = 0
		
# print max

def max_sum(tri):
	if len(tri) == 1:
		return tri[0]
	if len(tri) == 2:
		return tri[0][0] + max(tri[1][0],tri[1][0])
	return max(tri[len(tri)-1]) + max_sum(tri[:len(tri)-1])
	
def paths(tri):
		
#for h in range(1, 4):
 #   for x in range(1, 4):
  #  	tri
	
print max_sum([1])
print max_sum([[3],[7, 4]])
print max_sum([[3],[7, 4],[2, 4, 6]])
print max_sum([[3],[7, 4],[2, 4, 6], [8, 5, 9, 3]])

	