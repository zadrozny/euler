'''Problem 33: Digit canceling fractions The fraction 49/98 is a curious
fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by
cancelling the 9s. 

We shall consider fractions like, 30/50 = 3/5, to be
trivial examples. There are exactly four non-trivial examples of this type of
fraction, less than one in value, and containing two digits in the numerator
and denominator. 

If the product of these four fractions is given in its lowest
common terms, find the value of the denominator.'''

from numpy import prod

numerators   = []
denominators = []

for x in range(10, 99):
    for y in range(x+1, 100):
        try: 
            if str(x)[1] == str(y)[0]:
                if float(str(x)[0]) / int(str(y)[1]) == float(x) / y:
                    numerators.append(x)
                    denominators.append(y)
        except ZeroDivisionError: 
            pass 

print prod(denominators) / prod(numerators)