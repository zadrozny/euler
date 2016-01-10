'''Problem 39: Integer right triangles If p is the perimeter of a right angle
triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50} For which value of p <=
1000, is the number of solutions maximised?'''


from collections import Counter
from math import sqrt

cnt = Counter()                           # Perimeters and their counts

p = 1000                                  # p <= 1000

for a in range(1, p+1-2):                 # Offset by 1, subtract 2 for b & c
    for b in range(a+1, p - a): 
        c = sqrt(a**2 + b**2) 
        if c == int(c) and a+b+c <= 1000: # Is c an integer?
            cnt[a+b+int(c)] += 1          # If yes, increment given p

print cnt.most_common(1)[0][0]
