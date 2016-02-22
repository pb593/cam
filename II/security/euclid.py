#! /usr/local/bin/python3

def gcd(a, b):
	if a < b: # ensure a >= b to begin with
		(a, b) = (b, a)

	while(b > 0):
		a = a % b
		(a, b) = (b, a)

	return a

if __name__ == "__main__":
	print(gcd(36, 24))