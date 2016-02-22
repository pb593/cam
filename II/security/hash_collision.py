#! /usr/local/bin/python3
import hashlib
from random import randint, sample

alphabet_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,."

def sha1(input):
	return hashlib.sha1(input).hexdigest()

def sha1_trunc(input, n):
	return sha1(input)[0:n]

def find_collision():
	l = len(alphabet_string)
	A = ["".join(sample(alphabet_string, l)) for i in range(0, 6)]
	d = dict()
	i = [0, 0, 0, 0, 0, 0]
	for i[0] in range(0 , l):
		for i[1] in range(0, l):
			for i[2] in range(0, l):
				for i[3] in range(0, l):
					for i[4] in range(0, l):
						for i[5] in range(0, l):
							s = "".join([A[j][i[j]] for j in range(0, 6)])
							h = sha1_trunc(s, 10)
							if(d.has_key(h)):
								return (s, d[h])
							else:
								d[h] = s


if __name__ == "__main__":
	(x1, x2) = find_collision()

	print("Collision:")
	print("sha1(%s) = %s" % (x1, sha1(x1)))
	print("sha1(%s) = %s" % (x2, sha1(x2)))

		


	

