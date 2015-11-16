#! /usr/bin/python
# -*- coding: utf-8 -*-

alpha = ['a', 't', 'c', 'g'] # list of codons

e = [[0, 0, 0, 0], # just padding, nothing is emitted in starting state
     [0.25, 0.25, 0.25, 0.25],
     [0.1, 0.1, 0.4, 0.4] ]     #emission probabilities

T = [[0.0, 0.5, 0.5], # state 0 is the staring state
     [0.0, 0.8, 0.2], 
     [0.0, 0.4, 0.6]] # transition probabilities

seq = ["aactgcacatgcggcgcgcccgcgctaat", "gggcgcgggcgccccgcg"]

if __name__ == "__main__":
    
    for s in seq:
        l = len(s)
        V = [[0 for char in range(l + 1)] for state in range(3)]
        
        # initialisation
        V[0][0] = 1 # always start in the starting state
        
        # fill the Viterbi table
        for s_index in range(1, l + 1):
            for state in range(3):
                base_index = alpha.index(s[s_index - 1])
                V[state][s_index] = e[state][base_index] * \
                        max([ V[k][s_index-1] for k in range(3) ])
                
        # now, trace back choosing the max at each step
        l_states = []
        for rev_index in range(l, 0, -1):
            plist = [ V[k][rev_index] for k in range(3) ]
            max_p = max(plist)
            max_index = plist.index(max_p)
            
            l_states.insert(0, max_index)
            
        print "**************************************"
        print "Viterbi path for seq%d:" % (seq.index(s) + 1)
        print s
        print "".join(str(x) for x in l_states)
        print "**************************************"