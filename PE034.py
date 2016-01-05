#PE34.py
''' 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. Find the
sum of all numbers which are equal to the sum of the factorial of their
digits. Note: as 1! = 1 and 2! = 2 are not sums they are not included. '''


from numpy import prod

# First, find the upper limit, which will be a sequence
# of 9's larger than 9! * the number of digits in that sequence
places = 1
while True:
    if int("9" * places) > ( places * prod(range(1, 10)) ):
        upper_limit = int("9" * places)
        break 
    places += 1

print "The upper limit is: ", upper_limit


# Next, find and sum all numbers which are 
# equal to the sum of the factorial of their digits
summation = 0
for n in range(3, upper_limit):
    if sum([prod(range(1, int(x)+1)) for x in str(n)]) == n:
        summation += n


print summation 