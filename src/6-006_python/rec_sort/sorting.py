import os
import sys
from typing import List
module_path = os.path.normpath(os.path.dirname(__file__) + "/../../modules")
sys.path.append(module_path)

from idx import idx
import math

def insertionSort(A, ascending = True) -> List:
    """
    insertion sort (default ascending) 
    params:
    A (list) : list of numbers
    ascending (boolean): default true for ascending mode, set false for descending

    return list (list of numbers)
    """
    for j in range(2, len(A) + 1):
        key = A[idx(j)]
        # insert A[j] into the sorted sequences A[1... j - 1]
        i = j -1
        while i > 0 and (A[idx(i)] > key if ascending else A[idx(i)] < key):
            A[idx(i + 1)] = A[idx(i)]
            i -= 1
        A[idx(i + 1)] = key
    return A

def merge(lo, hi, ascending) -> List:
    """
    merge the divided array/list
    lo, hi (list) = list like of numbers
    ascending (boolean) = the order of the merge
    """
    maxRange = (len(lo) + len(hi))
    if ascending:
        lo.append(math.inf)
        hi.append(math.inf)
    else:
        lo.append(-math.inf)
        hi.append(-math.inf)
    
    # initialize index for lo and hi array
    i, j = 0, 0
    A = []
    for k in range(0, maxRange):
        if ascending:
            if lo[i] <= hi[j]:
                A.append(lo[i])
                i += 1
            else:
                A.append(hi[j])
                j += 1
        else:
            if lo[i] >= hi[j]:
                A.append(lo[i])
                i += 1
            else:
                A.append(hi[j])
                j += 1
    return A

def mergeSort(A, ascending = True) -> List:
    """
    merge sort 
    Parameters:
    A = array like of numeric 
    ascending (boolean): the order of the sort (default=True)
    """
    if len(A) > 1:
        mid = len(A)//2
        lo, hi = A[:mid], A[mid:len(A)]
        left = mergeSort(lo, ascending)
        right = mergeSort(hi, ascending)
        A = merge(left, right, ascending)
    return A