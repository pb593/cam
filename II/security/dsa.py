#!/usr/bin/python
import hashlib
from modexp import modexp
from cryptomath import findModInverse

P = 0x8df2a494492276aa3d25759bb06869cbeac0d83afb8d0cf7cbb8324f0d7882e5d0762fc5b7210eafc2e9adac32ab7aac49693dfbf83724c2ec0736ee31c80291
        
Q = 0xc773218c737ec8ee993b4f2ded30f48edace915f

G = 0x626d027839ea0a13413163a55b4cb500299d5522956cefcb3bff10f399ce2c2e71cb9de5fa24babf58e5b79521925c9cc42e9f6f464b088cc572af53e6d78802
        
        
Y = 0xeb772a91db3b69af90c5da844d7733f24270bdd11aac373b26f58ff528ef267894b1e746e3f20b8b89ce9e5d641abbff3e3fa7dedd3264b1b313d7cd569656c
        
Sigs = [(0x932eeb1076c85e522f02e15441fa371e3fd000ac, 
         0x8f4378d1b2877d8aa7c0687200640d4bba72f2e5,
         0x696de4ffb102249aef907f348fb10ca704a4b186),
     
        (0x42e43b612a5dfae57ddf5929f0fb945ae83cbf61,
         0x8f4378d1b2877d8aa7c0687200640d4bba72f2e5,
         0x25f87cbb380eb4d7244963e65b76677bc968297e)]


def sha1(input):
    return hashlib.sha1(input).hexdigest()

def F(x):
    return x % Q
    
def verify(h, r, s):   
    sInv = findModInverse(s, Q)
    vrf = F(pow(G, h*sInv, P) * pow(Y, r*sInv, P) % P)
    
    return (r == vrf)

if __name__ == "__main__":
    
    print("Part B\n")
    for h, r, s in Sigs:
        print("Message hash: %s" % h)
        print("r = %s" % r)
        print("s = %s" % s)
        
        if(verify(h, r, s)):
            print("Signature verified")
        else:
            print("Signature verification failed")
        print("-------------------------------------------------------------")
            
            
    print("\nPart E\n")
    h1 = Sigs[0][0]
    h2 = Sigs[1][0]
    s1 = Sigs[0][2]
    s2 = Sigs[1][2]
    r = Sigs[0][1]
    
    invDeltaS = findModInverse(s1-s2, Q)
    k = (h1 - h2) * invDeltaS % Q
    kInv = findModInverse(k, Q)
    
    rInv = findModInverse(r, Q)
    # secret key
    x = (k * s1 - h1) * rInv % Q
    
    h3 = int(sha1("Wednesday"), 16)
    print(h3)
    sig = ( kInv * (h3 + x * r) ) % Q
    
    if(verify(h3, r, sig)):
        print("Fake signature verified!")
    else:
        print("Fake signature failed to verify. Try again...")
    
     
        
        