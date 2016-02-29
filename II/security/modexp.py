#!/usr/bin/python
from math import *

def modexp(g, e, m):
    '''Calculates g^e mod m'''
    a = g
    b = 1
    pow2 = 1
    n = int(floor(log(e, 2)))
    for i in range(n+1):
        if int(floor(e / pow2)) % 2 == 1:
            b = (b * a) % m
        pow2 = pow2 * 2
        a = (a * a) % m
    
    return b 
        
    

if __name__ == "__main__":
    print(modexp(123456789, 987654321, 2**80 - 1))
    print(modexp(7, 2**521 - 1, 2**3217 - 1) % 10**8)