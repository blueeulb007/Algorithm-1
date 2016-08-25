__author__ = 'zhihao_liu'


"""
    This Script is for programming assignment 3
"""
import random
import copy


# I/O
filename = "kargerMinCut.txt"

f = open(filename)
OrigGraph = {} # Create a graph to represent the adjacent list
OrigEdgeList  = [] # keep track of the Edge List
for line in f:
    linetmp1 = line.split('\t')
    linetmp2 = [int(liter) for liter in linetmp1 if liter != '\n']

    OrigGraph[linetmp2[0]] = linetmp2[1:]

    for i in range(len(linetmp2[1:])):
        OrigEdgeList.append((linetmp2[0],linetmp2[1+i]))

NRun = 200000
NumCross = 10000000000000
for j in range(NRun):
    # For each simulation run, reset the following
    Graph     = copy.deepcopy(OrigGraph)
    EdgeList  = OrigEdgeList[:]
    N = len(Graph) # Num of nodes
    M = len(EdgeList) # 2 * NUMBER OF EDGES

    random.seed()
    # Run the randomized contraction algorithm
    while len(Graph)> 2:

        # Pick a remaining edge(u,v) uniformly
        edgeContractIdx = random.randint(0,M-1)
        edgeContract    = EdgeList[edgeContractIdx]
        V1Contract      = edgeContract[0]
        V2Contract      = edgeContract[1]

        # Merge U and V into a single vertex; without loss of generality, we always name the new merged Vertex the same name as V1
        # Need to do the following:
        # - Update the OrigGraph dictionary: add all the values of V2Contract to V1Contract; delete V2Contract entry in the dict; delete V2Contract in V1Contract entry; replace V2Contract with V1Contract in all other entries
        V2ContractVal = Graph[V2Contract]

        Graph[V1Contract].remove(V2Contract)
        Graph[V2Contract].remove(V1Contract)
        Graph[V1Contract].extend(Graph[V2Contract])

        del Graph[V2Contract]

        EdgeList = []
        for key in Graph:

            idx = [idxiter for idxiter in range(len(Graph[key])) if Graph[key][idxiter] == V2Contract]
            nidx = len(idx)
            for i in range(nidx):
                Graph[key][idx[i]] = V1Contract

            # remove self loop
            idx = [idxiter for idxiter in range(len(Graph[key])) if Graph[key][idxiter] == key]
            nidx = len(idx)
            for i in range(nidx):
                Graph[key].remove(key)

            # Reconstruct the EdgeList
            for i in range(len(Graph[key])):
                EdgeList.append((key,Graph[key][i]))

        # Update the number of edges
        M = len(EdgeList)

    # Number of crossings:
    NumCrossIter = M / 2

    if NumCrossIter < NumCross:
        NumCross = NumCrossIter

    if (j+1) % 1000 == 0:
        print("Already Ran %d simulations, the Min Cut so far is %d" % (j+1, NumCross))

print(NumCross)


