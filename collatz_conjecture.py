#Take any natural number n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. 
#Repeat the process (which has been called "Half Or Triple Plus One", or HOTPO) indefinitely. 
#The conjecture is that no matter what number you start with, you will always eventually reach 1.

def collatz(n,p=False):
	if p:
		tor = [n]
	else:
		tor = True
	while n != 1:
		if n % 2 == 0:
			n //= 2
		else:
			n = n * 3 + 1
		if p: tor.append(n)
	return tor

for n in range(1,101):
	print(collatz(n,True))