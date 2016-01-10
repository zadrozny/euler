'''Problem 39: Integer right triangles If p is the perimeter of a right angle
triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50} For which value of p <=
1000, is the number of solutions maximised?'''


best_p 		   =  0
solutions_best =  0


for perimeter in range(12, 1001): # Start with 3, 4, 5 triangle
	
    solutions_current = 0

    for a in range(1, perimeter/2):
        for b in range(a, perimeter-a):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                solutions_current += 1

    if solutions_current > solutions_best:
        solutions_best = solutions_current
        best_p = perimeter


print best_p