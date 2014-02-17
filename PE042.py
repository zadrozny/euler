#PE042.py

import string

letter_scores    = {letter: i+1 for i, letter in enumerate(string.uppercase)}

triangle_numbers = [0.5*n*(n+1) for n in range(50)] #50 is arbitrary; seems big enough


with open(r'ProjectEulerProblem42words.txt') as f: 
	words = f.readlines()


triangle_words = 0

for word in words[0].split(","):
	word_score = sum(letter_scores[letter] for letter in word[1:-1])
	if word_score in triangle_numbers:
		triangle_words += 1

print triangle_words