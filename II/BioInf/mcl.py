#! /usr/bin/python
import networkx as nx, re 
import numpy as np
import re, time
import os
import matplotlib.pyplot as plt

import pprint
pp = pprint.PrettyPrinter()

power = 2
inflation = 2

def roundup(mtx):   # smooth up the results
    for row in mtx:
        for elt in row:
            if elt > 0.99 and elt < 1.0:
                elt = 1.0
            elif elt > 0.0 and elt < 0.01:
                elt = 0.0
            else:
                pass

def printmtx(mtx):
    for row in mtx:
        print row

if __name__ == "__main__":
    g = nx.Graph() # create graph
    fname = 'mcl.conf'
    fname = os.path.abspath(fname)
    conf = open(fname, 'rt') # open graph config
    
    
    #populate graph according to config
    for line in conf:
        line = line.replace(' ', '').strip()
        #print "[line] %s$" % line
        if len(line) == 0 or line[0] == '#':
            continue # ignore this line
        else:
            node, desc = line.split(':')
            node = int(node)
            g.add_node(node)
            
            lpairs = desc.split('|')
            for s in lpairs: # s is something like "(12, 3)"
                matches = re.match(r'^\(([0-9]+),([0-9]+)\)$', s)
                destnode = int(matches.group(1))
                weight = int(matches.group(2))
                
                if(destnode not in g.nodes()): # if destnode not added yet
                    g.add_node(destnode) # add it

                g.add_edge(node, destnode, {'weight': weight})
    
    pos=nx.spring_layout(g)
    nx.draw(g, pos)
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()
    
    
    ### now the core of the MCL algo
    # first, create adjacency matrix
    l = len(g.nodes())
    adjmtx = [[0 for x in  range(0, l)] for x in range(0, l)]
    for (i, j) in g.edges():
        adjmtx[i-1][j-1] = g[i][j]['weight']
        adjmtx[j-1][i-1] = g[j][i]['weight']
    
    
    # normalise the matrix by rows
    for j in range(0, l):
        colsum = sum([adjmtx[x][j] for x in range(0, l)]) # sum of column
        for i in range(0, l):
            adjmtx[i][j] = round(float(adjmtx[i][j]) / float(colsum), 2)
                # divide each elt in column by sum of the column
    print "*********************************"
    print "Normalized adjacency matrix:"
    printmtx(adjmtx)
    print "*********************************"
    
    prev = None
    while(prev != adjmtx): # while the matrix is changing
        prev = adjmtx
        adjmtx = np.linalg.matrix_power(adjmtx, power) # take the relevant power of the mtx
        adjmtx = [[round(x ** inflation, 2) for x in row] for row in adjmtx] 
                                                                # power of each elt
    
    print "*********************************"
    print "Resulting matrix:"
    printmtx(adjmtx)
    print "*********************************"
    