#!/usr/bin/python

from modexp import modexp
from euclid import modinv
from cryptomath import findModInverse

P = int("0x8df2a494492276aa3d25759bb06869cbeac0d83afb8d0cf7cbb8324f0d7882e5d0762fc5b7210eafc2e9adac32ab7aac49693dfbf83724c2ec0736ee31c80291", 0)
        
Q = int("0xc773218c737ec8ee993b4f2ded30f48edace915f", 0)

G = int("0x626d027839ea0a13413163a55b4cb500299d5522956cefcb3bff10f399ce2c2e71cb9de5fa24babf58e5b79521925c9cc42e9f6f464b088cc572af53e6d78802", 0)
        
        
Y = int("0xeb772a91db3b69af90c5da844d7733f24270bdd11aac373b26f58ff528ef267894b1e746e3f20b8b89ce9e5d641abbff3e3fa7dedd3264b1b313d7cd569656c", 0)
        
Sigs = [(int("0x932eeb1076c85e522f02e15441fa371e3fd000ac", 0), 
         int("0x8f4378d1b2877d8aa7c0687200640d4bba72f2e5", 0),
         int("0x696de4ffb102249aef907f348fb10ca704a4b186", 0)),
     
        (int("0x42e43b612a5dfae57ddf5929f0fb945ae83cbf61", 0),
         int("0x8f4378d1b2877d8aa7c0687200640d4bba72f2e5", 0),
         int("0x25f87cbb380eb4d7244963e65b76677bc968297e", 0))]


def F(x):
    return x % Q

if __name__ == "__main__":
    
    for h, r, s in Sigs:
        print("Message hash: %s" % h)
        print("r = %s" % r)
        print("s = %s" % s)
        
        sInv = findModInverse(s, Q)
        vrf = F(pow(G, h*sInv, P) * pow(G, r*sInv, P) % P)
        
        print("Vrf: %s" % vrf)
        if(r == vrf):
            print("Signature verified")
        else:
            print("Signature verification failed")
        
        