# Current version
$ python -m timeit -s 'import PE009'
31875000
100000000 loops, best of 3: 0.012 usec per loop

# Old version
$ python -m timeit -s 'import PE009'
200 plus 375 plus 425 equals 1000
100000000 loops, best of 3: 0.0127 usec per loop
