# PE4.py
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers
'''

# The smallest 3-digit number is 100
# The largest is 999

print max(x*y for x in xrange(100, 1000) 
              for y in xrange(100, x + 1) 
              if str(x*y) == str(x*y)[::-1])

