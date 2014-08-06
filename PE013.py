'''Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.'''

print str(sum(int(line) for line in number.split('\n')))[:10]
