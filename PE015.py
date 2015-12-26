#PE15.py 
''' 
Lattice Paths: How many routes are there through 
a 20x20 grid [from the top left to the bottom right corner]? 
'''

width, height = 20, 20

paths = {}

for y in range(height + 1): 
    for x in range(width + 1): 
        if 0 in (x, y): 
            # All coordinates on left / top perimeter have one path:
            paths[(x, y)] = 1
        else: 
            # incoming paths = paths from left + paths from above:
            paths[(x, y)] = paths[(x - 1), y] + paths[(x, y - 1)]


print paths[(20, 20)]