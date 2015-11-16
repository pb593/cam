#! /usr/bin/python
# -*- coding: utf-8 -*-

from math import exp, log

alpha = ['a', 't', 'c', 'g'] # list of codons

e = [[0, 0, 0, 0], # just padding, nothing is emitted in starting state
     [0.25, 0.25, 0.25, 0.25],
     [0.1, 0.1, 0.4, 0.4] ]     #emission probabilities

T = [[0.0, 0.5, 0.5], # state 0 is the staring state
     [0.0, 0.8, 0.2], 
     [0.0, 0.4, 0.6]] # transition probabilities
     
seq = ["aactgcacatgcggcgcgcccgcgctaat", "gggcgcgggcgccccgcg"]

def calcProb(s):
    l = len(s)
    F = [[0 for char in range(l + 1)] for state in range(3)]
    
    # initialisation
    F[0][0] = 1 # always start in the starting state
    
    # fill the Forward table
    for s_index in range(1, l + 1):
        for state in range(3):
            base_index = alpha.index(s[s_index - 1])
            F[state][s_index] = e[state][base_index] * \
                    sum([ F[k][s_index-1] * T[k][state] for k in range(3) ])
            
    P = sum([F[k][l] for k in range(3)]) # sum all elements in last column
    
    return P
    
def calcLogProb(s):
    
    def toLog(p1):
        assert(p1 >= 0)
        if (p1 == 0.0):
            return float('inf')
        else:
            return -log(p1)
    
    def toReal(p1):
        return exp(-p1)
    
    l = len(s)
    Flog = [[toLog(0) for char in range(l + 1)] for state in range(3)]
    
    # initialisation
    Flog[0][0] = toLog(1.0) # always start in the starting state (p = 1)
    
    # fill the Forward Log Table
    for str_index in range(1, l + 1):
        for state in range(3):
            base_index = alpha.index(s[str_index - 1])
            Flog[state][str_index] = toLog(e[state][base_index]) + \
                    toLog(sum([toReal(Flog[k][str_index-1] + \
                        toLog(T[k][state])) for k in range(3) ]))
            
    Plog = toLog(sum([toReal(Flog[k][l]) for k in range(3)]))
    return Plog

if __name__ == "__main__":
    
    for s in seq:
        P = calcProb(s)
        Plog = calcLogProb(s)
        
        print "**************************************"
        print "Probability of seq%d: %f" % (seq.index(s) + 1, P)
        print "Log probability of seq%d: %f (= %f)" % (seq.index(s) + 1, Plog,
                                                                    exp(-Plog))
        print "**************************************"