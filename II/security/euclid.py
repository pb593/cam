#! /usr/local/bin/python3

def gcd(a, b):
	(a0, b0) = (a, b)

	while(b > 0):
		a = a % b
		(a, b) = (b, a)

	print("Standard GCD")
	print("gcd(%d, %d)= %d\n" % (a0, b0, a))
	return a

def egcd(a, b):

	(a0, b0) = (a, b)

	(aa, ab) = (1, 0)
	(ba, bb) = (0, 1)

	while(True):
		q = a / b

		if(a == q * b):
			print("Extended Euclid")
			print("gcd(%d, %d) = %d = (%d) * (%d) + (%d) * (%d)\n" % (a0, b0, b, ba, a0, bb, b0))
			return (b, ba, bb)
		else:
			(a, aa, ab, b, ba, bb) = (b, ba, bb, a - b*q, aa - q*ba ,ab - q*bb)


if __name__ == "__main__": 
	gcd(36, 24)
	egcd(733810016255931844845,1187329547587210582322)