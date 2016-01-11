#PE042.py

from requests import get
import string

r = get('https://projecteuler.net/project/resources/p042_words.txt').text

# Clean up: split, convert unicode to str, strip extra quotes
words = [word.strip('"') for word in map(str, r.split(','))]

# Create letter scores lookup table
letter_scores = {letter: i for i, letter in enumerate(string.uppercase, 1)}

# Convert words to scores
word_scores = [sum(letter_scores[letter] for letter in word) for word in words]

# Choose number of triangle numbers with largest word score (could be optimized)
limit = max(word_scores) 

# Generate triangle numbers
triangle_numbers = [0.5*n*(n+1) for n in xrange(limit)] 

# Count triangle words
print len([w for w in word_scores if w in triangle_numbers])
