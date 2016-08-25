__author__ = 'zhihao_liu'

"""
    This script implements two problems in assignment 6
"""
import heapq

#### Question 1 - Two Sum Problem

filenames = "algo1-programming_prob-2sum.txt"
f = open(filenames)
InterSet = set()
for line in f:
    tmp = line.splitlines()
    Iter = int(tmp[0])
    InterSet.add(Iter)
f.close()



numDistinct = 0
t = -10000
while t <= 10000:
    print(t)
    for interiter in InterSet:
        if ( t - interiter) in InterSet and ( t - interiter) != interiter:
            numDistinct += 1
            break
    t += 1

print(numDistinct)


#### Question 2 - Median Maintainence
filename =  "Median.txt"
f = open(filename)
h = []
medianSum = 0
k = 0
for line in f:
    k += 1
    print(k)
    tmp = line.splitlines()
    Iter = int(tmp[0])
    heapq.heappush(h,Iter)
    if k % 2 == 1: ## odd
        listIter  = heapq.nsmallest(int((k+1)/2), h)
    else: ## even
        listIter  = heapq.nsmallest( int(k/2), h)

    medianSum += listIter[-1]

f.close()

print( medianSum % 10000)