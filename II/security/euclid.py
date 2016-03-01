#! /usr/local/bin/python3

def gcd(a, b, out):
	(a0, b0) = (a, b)

	while(b > 0):
		a = a % b
		(a, b) = (b, a)

	if(out):
		print("Standard GCD")
		print("gcd(%d, %d)= %d\n" % (a0, b0, a))

	return a

def egcd(a, b, out):

	(a0, b0) = (a, b)

	(aa, ab) = (1, 0)
	(ba, bb) = (0, 1)

	while(True):
		q = a / b

		if(a == q * b):
			if(out):
				print("Extended Euclid")
				print("gcd(%d, %d) = %d = (%d) * (%d) + (%d) * (%d)\n" 
													% (a0, b0, b, ba, a0, bb, b0))
			return (b, ba, bb)
		else:
			(a, aa, ab, b, ba, bb) = (b, ba, bb, a - b*q, aa - q*ba ,ab - q*bb)

def modinv(a, n, out):
	(rst, x, y) = egcd(a, n, False)
	if(rst != 1):
		if(out):
			print("Inverse for %d does not exist in Z(%d)" % (a, n))
		return None
	else:
		if(out):
			print("Inverse for %d in Z(%d) is %d" % (a, n, x % n))

if __name__ == "__main__": 
	gcd(36, 24, True)
	egcd(733810016255931844845,1187329547587210582322, True)
	modinv(806515533049393, 1304969544928657, True)
	modinv(892302390667940581330701, 1208925819614629174706111, True)
