__author__ = 'zhihao_liu'
"""
    This script implements the Dijkstra's shortest path algorithm
     1 ) Naive way - O(m*n) running time
     2 ) heap based - O(m * log(n) ) running time - TBD
"""

# I/O - Load Data
filename = "dijkstraData.txt"
f = open(filename)
OrigGraph = {}

for line in f:
    tmp = line.splitlines()
    tmp = tmp[0]
    tmp = tmp.split('\t')
    foo = tmp.pop() # the last element is just " "
    keytmp = int(tmp[0])

    # Orig Graph
    if not OrigGraph.__contains__(keytmp):
        OrigGraph[keytmp] = []

    for tmpIter in tmp[1:]:
        tmpIter = tmpIter.split(',')
        OrigGraph[keytmp].append((int(tmpIter[0]), int(tmpIter[1])))


f.close()

print("Reading Graph Done")

# Naive Implementation
V = set(OrigGraph.keys())
X = {1} # Source node is 1
distGraph = {}
for key in OrigGraph:
    if key == 1:
        distGraph[key] = 0
    else:
        distGraph[key] = 1000000

print("Initilization Done - Entering to the loop")

while X != V:
    w = None
    dijCrit = []
    for v in X:
        # We only select the edges v-w where v in X and w not in w
        vEdges  = OrigGraph[v]
        vEdges  = [(vx, d) for (vx, d) in vEdges if vx not in X]
        dijCritIter = [(vx,d + distGraph[v] ) for (vx, d) in vEdges ]
        dijCrit.extend(dijCritIter)

    # Apply the Dijstra's Greedy Criteria
    dijCrit = sorted(dijCrit, key = lambda x:x[1])

    w = dijCrit[0][0]
    distGraph[w] = dijCrit[0][1]

    X.add(w)


print(distGraph)
