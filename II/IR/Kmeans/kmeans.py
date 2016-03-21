#!/usr/bin/python
import numpy as np
import math
import copy

FNAME = "docs.txt"


def dist(v1, v2):
    return 1 - np.dot(v1, v2)  # 1 / SIM(d1, d2)


def centroids_equal(old, new):
    if len(old) != len(new):
        return False  # not equal
    else:
        for i in range(len(new)):
            if not np.array_equal(new[i], old[i]):
                return False  # not equal

        return True  # equal

def clusterings_equal(new, old):
    if len(old) != len(new):
        return False  # not equal
    else:
        for i in range(len(new)):
            if not new[i] == old[i]:
                return False  # not equal

        return True  # equal

if __name__ == "__main__":

    # pre-processing
    doc_count = 0
    terms = set()
    docs = list()

    with open(FNAME) as file:
        for doc in file:
            doc_count += 1  # count up the docs
            ts = doc.split()  # split on whitespace
            docs.append(ts)  # each doc is a list of terms
            terms.update(ts)  # add to set of terms, doing de-duplication

    terms = list(terms)  # give some ordering to terms

    # create logartithmic term freq table
    vects = list()
    for d in docs:
        tf = [(math.log(1 + d.count(t)) if d.count(t) > 0 else 0) for t in terms]  # 1 + log(tf(t, d))
        tf = np.array(tf) / np.linalg.norm(tf)  # cosine normalization
        vects.append(tf)

    # K-means
    K = 2

    Cs = [np.array([np.random.uniform(0, 1) for dim in range(len(terms))]) for k in range(K)]  # take centroids randomly
    clusters = [set() for k in range(K)]
    iter_cnt = 0
    while (True):
        # re-assignment
        clusters_old = copy.deepcopy(clusters)
        clusters = [set() for k in range(K)]
        for i in range(len(vects)):
            doc = vects[i]
            min_dist = float("inf")
            j_min = 0
            for j in range(K):
                d = dist(doc, Cs[j])
                if (d < min_dist):
                    min_dist = d
                    j_min = j

            clusters[j_min].add(i)  # add index of the doc to appropriate cluster

        if(clusterings_equal(clusters, clusters_old)): # if clusterings have not changed – exit
            break

        # re-compute centroids
        Cs_old = copy.deepcopy(Cs)
        for i in range(K):
            xs = [vects[j] for j in clusters[i]]  # sum of all vectors currently assigned to a cluster
            Cs[i] = sum(xs) / len(xs)  # average of all vectors assigned to cluster

        iter_cnt+=1 # increase iteration count

    print("Clusters")
    for i in range(K):
        print("%d: %s" % (i, list(clusters[i])))
    print("Iteration count: %d" % iter_cnt)