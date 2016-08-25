__author__ = 'zhihao_liu'

"""
    Driver script to run the SCC algo
"""

import SCC

filename = "SCC.txt"

(OrigGraph, ReverseGraph) = SCC.LoadGraphs(filename)

print("Done with Constructing Graph and Reverse Graph")

# First DFS loop to get the finish time
finish_time_dic = SCC.DFSIterativeFindFinishingTime(ReverseGraph)
print("Done with First DFS Loop to Calculate the Finishing Time")

# Sort the finish time
keyValPairSorted = sorted([(value,key) for (key, value) in finish_time_dic.items() ], reverse = True)
KeyList = [k for (foo,k) in keyValPairSorted]
print("Done with Sorting the Finishing time and Value")

# Second DFS loop to get the Strong Connected componnets
N = len(KeyList)
LeaderDic = {}
visited = set()
OrigKey = list(OrigGraph.keys())

for v in KeyList:
    LeaderDic[v] = 0
    if OrigGraph.__contains__(v):
        if not v in visited:
                SCC.DFSIterative(OrigGraph,v,visited, LeaderDic)

print("Done with Second DFS Loop")

# Number of first five
Leader = list(LeaderDic.values())

Leader.sort(reverse=True )

print("Final Results")
print(Leader[0:5])


