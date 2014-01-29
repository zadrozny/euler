#PE15.py 
''' Lattice Paths: How many routes are there through 
a 20x20 grid [from the top left to the bottom right corner]? 
'''

width, height = 20, 20

d = {}
for y in range(height + 1): 
    for x in range(width + 1): 
        if 0 in (x, y): 
            #All coordinates on edge have one path:
            d[(x, y)] = 1
        else: 
            #incoming paths = paths from left + paths from above:
            d[(x, y)] = d[(x - 1), y] + d[(x, y - 1)]


print d[(20, 20)]