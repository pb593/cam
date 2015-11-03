#!/usr/bin/python
import networkx as nx

def func(l):
    l[0] = 500
    
if __name__ == "__main__":
    l = [1, 2, 3]
    func(l)
    
    print l
