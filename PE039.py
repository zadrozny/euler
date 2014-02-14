'''Problem 39: Integer right triangles If p is the perimeter of a right angle
triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50} For which value of p <=
1000, is the number of solutions maximised?'''


limit 		   = 10
best_p 		   =  0
solutions_best =  0


for p in range(3, 1001):
	
	solutions_current = 0

	for a in range(1, p):
		for b in range(a, p - a):
			c = p - a - b
			if a**2 + b**2 == c**2:
				solutions_current += 1

	if solutions_current > solutions_best:
		solutions_best = solutions_current
		best_p = p


print best_p