#!/usr/bin/python
# Alignment, global and local

import argparse, pprint, sys

pp = pprint.PrettyPrinter()

class Pointer:
    none, up, left, diag = range(4)
    

def align(str1, str2, params_dict): # creates the alignment matrix and returns it
    match = params_dict['match']
    gap = params_dict['gap']
    mismatch = params_dict['mismatch']

    l1 = len(str1)
    l2 = len(str2)
     
    mtx = [[(0, Pointer.none) for x in range(l2 + 1)] for x in range(l1 + 1)]
     
    #init the matrix
    for i in range(0, l1 + 1):
        mtx[i][0] = (i * gap, Pointer.up)
         
    for j in range(0, l2 + 1):
        mtx[0][j] = (j * gap, Pointer.left)
     
    # do the matrix computation
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            up_score = mtx[i-1][j][0] + gap
            left_score = mtx[i][j-1][0] + gap
            diag_score = mtx[i-1][j-1][0] + (match if str1[i-1] == str2[j-1] else mismatch)
            if max(up_score, left_score, diag_score) == up_score:
                mtx[i][j] = (up_score, Pointer.up)
            elif max(up_score, left_score, diag_score) == left_score:
                mtx[i][j] = (left_score, Pointer.left)
            else: # diag is max
                mtx[i][j] = (diag_score, Pointer.diag)
                
    return mtx
    
    
def pretty_print(str1, str2, mtx):
    # print both strings, aligned
    al1 = ""
    al2 = ""
    i, j = (len(str1), len(str2))
    while i > 0 or j > 0:
         if mtx[i][j][1] == Pointer.diag:
             al1+=str1[i-1]
             al2+=str2[j-1]
             i-=1
             j-=1
         elif mtx[i][j][1] == Pointer.up:
             al1+=str1[i-1]
             al2+='_'
             i-=1
         elif mtx[i][j][1] == Pointer.left:
             al1+='_'
             al2+=str2[j-1]
             j-=1
         else:
             #something bad happened
             print "POLUNDRA!!!"
             exit(-1)
             
      
    al1 = ''.join(al1[::-1]) # reverse
    al2 = ''.join(al2[::-1]) # reverse
    print "%s" % al1
    print "%s" % al2
    
    
if __name__ == "__main__":
    
    # try global alignment first
    str1 = "CATGT"
    str2 = "ACGCTG"
    print "*******************************************"
    print "Global alignment: %s <-> %s" % (str1, str2)
    
    mtx = align(str1, str2, {'match' : 2, 'gap': -1, 'mismatch' : -1})
    pretty_print(str1, str2, mtx)
    
    print "Score: %d" % mtx[len(str1)][len(str2)][0]
    print "*******************************************"
    
    
    # now, local alignment
    str1 = "TAATA"
    str2 = "TACTAA"
    print "*******************************************"
    print "Local alignment: %s <-> %s" % (str1, str2)
    
    mtx = align(str1, str2, {'match' : 1, 'gap': -2, 'mismatch' : -1}) # gaps at the end 
    pretty_print(str1, str2, mtx)
    
    print "Score: %d" % mtx[len(str1)][len(str2)][0]
    print "*******************************************"
             
             
