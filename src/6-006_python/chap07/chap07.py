import os
import sys

module_path = os.path.normpath(os.path.dirname(__file__) + "/../../modules")
sys.path.append(module_path)

from idx import idx

def partition(A, p, r):
    """
    process the partition in the quick sort function.
    param: 
    A (array) = list of numbers, p (int) = index in the list, r (int)=index in the list (p < r)
    
    return: array
    """
    x = A[idx(r)]
    i = p - 1
    # loop from p to r-1 (inclusive)
    for j in range(p, r):
        if A[idx(j)] <= x:
            i += 1
            temp = A[idx(i)]
            A[idx(i)] = A[idx(j)]
            A[idx(j)] = temp
    
    temp2 = A[idx(i + 1)]
    A[idx(i + 1)] = A[idx(r)]
    A[idx(r)] = temp2
    return i + 1, A

def quicksort(A, p, r):
    """
    quicksort of an Array
    param: 
    A (array): list of numbers, p (int): index in the Array, r (int): index in the Array (p < r)

    return: array
    """
    if p < r :
        q, A = partition(A, p, r)
        # do this recursively:
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    
    return A

if __name__ == '__main__':
    inputArray = input("input initial array: ")
    initA = []
    for number in inputArray.split(","):
        initA.append(int(number))

    print(quicksort(initA, 1, len(initA)))