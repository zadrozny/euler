"""
Project Euler Problem #79
==========================

A common security method used for online banking is to ask the user for
three random characters from a passcode. For example, if the passcode was
531278, they may asked for the 2nd, 3rd, and 5th characters; the expected
reply would be: 317.

The text file, keylog.txt [http://projecteuler.net/project/keylog.txt],
contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of unknown
length.
"""



L = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 
     368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 
     736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 
     318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 
     890, 362, 319, 760, 316, 729, 380, 319, 728, 716]


# L = list(set(L)) removes 17 duplicates and produces: 

L = [129, 389, 769, 790, 160, 289, 290, 680, 689, 690, 180, 
     316, 318, 319, 710, 716, 162, 718, 719, 720, 728, 729, 
     731, 890, 736, 362, 620, 368, 168, 629, 760, 762, 380]


# No 4 or 5
import string
print sorted(list(set(string.digits) - set(''.join(map(str, L)))))



# No duplicate digits, ie, digits that follow each other:

d = {d: [] for d in digits}


for n in L:
    n = str(n)

    if n[1] not in d[n[0]]:
        d[n[0]].append(n[1])
    
    if n[2] not in d[n[0]]:
        d[n[0]].append(n[2])
    
    if n[2] not in d[n[1]]:
        d[n[1]].append(n[2])

for k, v in d.items():
    for i in v:
        if k in d[i]:
            print k, i # Would mean there's a duplicate digit 

# A bit of manual fiddling produces: 

73162890