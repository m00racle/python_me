import os
import sys
module_path = os.path.normpath(os.path.dirname(__file__) + "/../../modules")
sys.path.append(module_path)

from idx import idx

def insertionSort(A, ascending = True):
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