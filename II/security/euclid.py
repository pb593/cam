#! /usr/local/bin/python3

def gcd(a, b):
	if a < b: # ensure a >= b to begin with
		(a, b) = (b, a)

	while(b > 0):
		a = a % b
		(a, b) = (b, a)

	return a

def egcd(a, b):
	if a < b: # ensure a >= b to begin with
		(a, b) = (b, a)

	(a0, b0) = (a, b)

	(aa, ab) = (1, 0)
	(ba, bb) = (0, 1)

	while(True):
		q = a / b

		if(a == q * b):
			return (b, ba, bb)
		else:
			(a, aa, ab, b, ba, bb) = (b, ba, bb, a - b*q, aa - q*ba ,ab - q*bb)


if __name__ == "__main__":
	print(egcd(733810016255931844845,1187329547587210582322))