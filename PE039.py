'''Problem 39: Integer right triangles If p is the perimeter of a right angle
triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50} For which value of p <=
1000, is the number of solutions maximised?'''


from collections import Counter
from math import sqrt

cnt = Counter()

p = 1000 # Perimeter

for a in range(1, p + 1 - 2):  
    for b in range(a+1, p - a):
        root = sqrt(a**2+b**2) 
        if root == int(root) and a+b+root <= 1000:
            cnt[a+b+root] += 1

print int(cnt.most_common(1)[0][0])
