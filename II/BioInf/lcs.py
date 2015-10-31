#!/usr/bin/python

# Longest Common Subsequence using dynamic programming
import pprint, time, os

pp = pprint.PrettyPrinter()


if __name__ == "__main__":
    s1 = "abdce"
    s2 = "abecdx"
    
    l1 = len(s1)
    l2 = len(s2)
    
    mtx = [[0 for x in range(l2 + 1)] for x in range(l1 + 1)] 
    
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            mtx[i][j] = max(mtx[i-1][j], mtx[i][j-1], mtx[i-1][j-1] + 1 if s1[i-1] == s2[j-1] else 0)
            os.system("clear")
            pp.pprint(mtx)
            time.sleep(0.5)
            
            
    print "The longest common subsequence of %s and %s has length %d" % (s1, s2, mtx[l1][l2])
            
    
            
