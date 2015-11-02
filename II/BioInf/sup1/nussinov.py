#!/usr/bin/python
# Nussinov RNA structure prediction

import pprint
pp = pprint.PrettyPrinter()

def delta(seq, i, j):
    # returns 1 if (a,b) is a base pair and 0 otherwise
    if(abs(i - j) == 1): # penalise zero-length loops severely
        return -100500
    else:
        return abs(i - j) if ((seq[i], seq[j]) in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]) else 0

def fold(seq):
    l = len(seq)
    gamma = [[0 for x in range(l)] for x in range(l)]
    
    # init the matrix
    for i in range(1, l):
        gamma[i][i - 1] = 0
    for i  in range(0, l):
        gamma[i][i-1] = 0
    
    
    # fill the matrix (indices are 1-based)
    for i in range(l - 1, 0, -1): # from l-1st to 1st symbol
        for j in range(i + 1, l + 1): # from i + 1st to lth symbol, inclusive
            below = gamma[i - 1 + 1][j - 1]
            left = gamma[i - 1][j - 1 - 1]
            diag = gamma[i - 1 + 1][j - 1 - 1] + delta(seq, i - 1, j - 1)
            
            # bifurcation
            biflist  = [gamma[i - 1][k - 1] + gamma[k - 1 + 1][j - 1] for k in range(i + 1, j)]
            bif = max(biflist) if len(biflist) != 0 else None
            
            
            gamma[i - 1][j - 1] = max([below, left, diag, bif])
            
    #pp.pprint(gamma)
    
    
    # backtracking part
    rst = ['.' for i in range(0, l)]
    stack = [(1, l)] # indices are 1-based here
    while(len(stack) > 0):
        i, j = stack.pop()
        if i > j:
            continue
        elif(gamma[i - 1 + 1][j - 1] == gamma[i - 1][j - 1]):
            stack.append((i + 1, j))
        elif(gamma[i - 1][j - 1 - 1] == gamma[i - 1][j - 1]):
            stack.append((i, j - 1))
        elif(gamma[i - 1 + 1][j - 1 - 1] + delta(seq, i - 1, j - 1) == gamma[i - 1][j - 1]):
            rst[i - 1] = "("
            rst[j - 1] = ")"
            stack.append((i + 1, j - 1))
        else:
            for k in range(i + 1, j):
                if gamma[i-1][k-1] + gamma[k - 1 + 1][j - 1] == gamma[i - 1][j - 1]:
                    stack.append((k + 1, j))
                    stack.append((i, k))
                    break
                    
                    
                    
    return ''.join(rst)


if __name__ == "__main__":
    
    strings = ["GGGAAAUCC", "CCUUAAGGAGAGAGCCUUAAGG", "AAGUUCGGUCC", "AAAUUU"]
    
    for s in strings:
        r = fold(s)
        print "*******************************************"
        print "Folded RNA: "
        print "%s" % s
        print "%s" % r
        print "*******************************************"