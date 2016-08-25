__author__ = 'zhihao_liu'
import math
import statistics
import random

################### Programming Assignment 1 ########################
# Merge Sort: o(nlogn) running time
# plus counting the number of inversions
def MergeSort( Arry ):
   N = len(Arry)
   if N <= 1:
       return (Arry, 0)
   else:
       M = math.ceil( N / 2)
       (SubArry1, num1) =  MergeSort( Arry[0: M] )
       (SubArry2, num2)  = MergeSort( Arry[M:] )
       (MergedArry, numcount) = MergeSortHelper(SubArry1, SubArry2)
       return ( MergedArry, num1 + num2 + numcount )


def MergeSortHelper(Arry1, Arry2):
    n1 = len(Arry1)
    n2 = len(Arry2)
    n3 = n1 + n2
    i = 0
    j = 0
    numcount = 0
    MergedArry = []
    for k in range(n3):
        if i < n1 and j < n2:
            if Arry1[i] <= Arry2[j]:
                MergedArry.append(Arry1[i])
                i += 1
            else:
                MergedArry.append( Arry2[j])
                j += 1
                #count the number of inversions
                numcount += (n1 - i)
        elif i == n1:
            MergedArry.append( Arry2[j])
            j +=1
        else:
            MergedArry.append(Arry1[i])
            i +=1

    return (MergedArry, numcount)

# Test Merge Sort
print(MergeSort ([] ) ) # Empty
print(MergeSort([1,1,1,1]))
print(MergeSort( [1,3,2,6,2,3,1]))


# QuickSort
def QuickSort(Arry, Opt):
    N = len(Arry)
    Ncompare = 0
    if N <= 1:
        return (Arry, Ncompare)
    else:

        (IdxP,p) =  QuickSortChoosePivot(Arry,Opt)

        # Pre-processing

        Arry[IdxP] = Arry[0]
        Arry[0] = p

        # Partition around p
        IdxRecurse = QuickSortPartition(Arry, 0, len(Arry)-1)

        Ncompare += len(Arry)-1

        # Recursive Calls:
        # Here should pay attention: if List gets sliced - it is a Shawdow copy
        (Arry[0:IdxRecurse], NcompareLeft)    = QuickSort(Arry[0:IdxRecurse],Opt)
        (Arry[IdxRecurse+1:], NcompareRight)  = QuickSort(Arry[IdxRecurse+1:], Opt)

        return (Arry, Ncompare + NcompareLeft + NcompareRight)


################### Programming Assignment 2 ########################
def QuickSortChoosePivot(Arry, Opt):
    # Return (Idx(Pivot), PivotValue)
    # At least one element in Arry
    if Opt == 1: # First Element
        return (0, Arry[0])
    elif Opt == 2: # Last Element
        return (len(Arry) -1, Arry[-1])
    elif Opt == 3: # Medium of the three
        nIdx1 = 0
        nIdx2 = len(Arry) - 1
        nIdx3 = math.floor( (len(Arry) - 1)/2)

        nIdxL = [nIdx1, nIdx2, nIdx3 ]
        nL  = [Arry[idxIter] for idxIter in nIdxL]
        p = statistics.median(nL)
        idxP = nIdxL[nL.index(p)]
        return (idxP, p)

    else: # Random Selection
        idxP = random.randint(0, len(Arry) - 1)
        return(idxP, Arry[idxP])

def QuickSortPartition(Arry, l, r):

    p = Arry[l]
    i = l + 1
    for j in range(i, r+1):
        if Arry[j] < p:
            tmp = Arry[j]
            Arry[j] = Arry[i]
            Arry[i] = tmp
            i += 1

    tmp = Arry[l]
    Arry[l] = Arry[i-1]
    Arry[i-1] = tmp

    # Finally we need to return the idx of the pivot after partition for recursive calls
    return i-1

filename = "QuickSort.txt"
f = open(filename)
data = f.readlines()
f.close()
L = [int(dataIter) for dataIter in data]
# Make two copies
L1 = L[:]
L2 = L[:]
# L = list(range(10000))
# random.shuffle(L)
# print(L)
# # L = [2, 4, 0, 3, 1]
# print(QuickSort(L, 1)[1])
# print(QuickSort(L1,2)[1])
print(QuickSort(L1,3)[1])
print(QuickSort(L2,4)[1])
