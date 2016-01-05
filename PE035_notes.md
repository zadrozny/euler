# Lists vs sets

In line 8, I cast the primes into a set because there is a huge slowdown from calling issubset on a list (line 16). 

This likely causes slower iteration in line 12, but the trade-off is worth it. Without it, the program runs for well over a minute; with it, it runs in under 3 secs.

I could use a list for the for loop and a create a separate set for use in line 16, but this would require allocating more memory, which isn't worth it.

Source: 

http://stackoverflow.com/a/2831242/1366410 
	
	Sets are significantly faster when it 	comes to determining if an object is present in the set (as in x in s), but are slower than lists when it comes to iterating over their contents.