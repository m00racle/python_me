import heap1
import math

import os
import sys

module_path = os.path.normpath(os.path.dirname(__file__) + "/../../modules")
sys.path.append(module_path)

from idx import idx

def heapMax(A):
    return A[idx(1)]

def heapExtractMax(A, size):
    """
    # implements the extract max operations
    # parameters: 
    # A = list, 
    # size = int represent the size of A under operation.
    """
    # 1. if A.heap-size < 1:
    # 2. error "heap underflow"
    if size < 1: raise ValueError("heap underflow")
    
    # 3. max = A[1]:
    maxElement = A[idx(1)]

    # 4. A[1] = A[A.heap-size]
    A[idx(1)] = A[idx(size)]

    # 5. A.heap-size = A.heap-size - 1
    size -= 1

    # 6. MAX-HEAPIFY(A,1,SIZE)
    A = heap1.maxHeapify(A, 1, size)

    # 7. return max
    return maxElement

def heapIncreaseKey(A, i, key):
    """
    implements the heap increase key operation
    parameters:
    A (list) : the list to be priority queue
    i: element (index start from 1 not 0) which value will be subtituted
    key (number): the number to be inserted subtituting the current elemen value
    """
    # 1. if key < A[i]
    # 2.   Error: "new key is smaller than current element's value"
    if key < A[idx(i)]: raise ValueError("new key is smaller than current element value")

    # 3. A[i] = key
    A[idx(i)] = key

    # 5. while i > 1 and A[PARENT(i)] < A[i]:
    while i > 1 and A[idx(heap1.parent(i))] < A[idx(i)]:
        # 6. exchange A[PARENT(i)] with A[i]
        temp = A[idx(heap1.parent(i))]
        A[idx(heap1.parent(i))] = A[idx(i)]
        A[idx(i)] = temp

        # i = parent(i)
        i = heap1.parent(i)

    return A

def maxHeapInsert(A, key):
    """
    run max heap insert operation
    parameter: 
    A (list) = list of max heapified numvbers
    key (int) = number to be added into exiting list and heapified
    """
    # 1. A.heap-size = A.heap-size + 1
    # 2. A[A.heap-size] = -inf
    # note: these steps will be using the .appemd() function
    A.append(-math.inf)
    # note: -math.inf = negative infinity

    return heapIncreaseKey(A, len(A), key)
