#PE18.py 
'''By starting at the top of the triangle below and moving to adjacent 
numbers on the row below...Find the maximum total from top to bottom
of the triangle below.'''


t = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

#Enter the triangle into a list of lists, from base to top:
triangle = [[int(n) for n in line.split()] 
			for line in reversed(t.split('\n')) if line]

def chooseLargest(row):
	'''Chooses largest of two neighbors (i vs i+1) 
	and returns this row as long as the one above it.'''

	for i, n in enumerate(row[:-1]):
 		row[i] = max([n, row[i+1]])
 	return row[:-1] 				#Remove last element


def addColumns(currentRow, nextRow):
	'''Adds each number to the one directly above it.'''

	for i, n in enumerate(currentRow): 
		nextRow[i] = n + nextRow[i]


#Iterate over the triangle from **top to bottom**:
for i, row in enumerate(triangle[:-1]):
	current = chooseLargest(row)
	addColumns(current, triangle[i+1])


maxTotal = triangle[-1][0]

print maxTotal
