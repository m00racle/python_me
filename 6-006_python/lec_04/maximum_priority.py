import heap1

ind = heap1.ind

def heapMax(A):
    return A[ind(1)]

def heapExtractMax(A, size):
    # implements the extract max operations
    # parameters: A = list, size = int represent the size of A under operation.
    # 1. if A.heap-size < 1:
    # 2. error "heap underflow"
    if size < 1: raise ValueError("heap underflow")
    
    # 3. max = A[1]:
    maxElement = A[ind(1)]

    # 4. A[1] = A[A.heap-size]
    A[ind(1)] = A[ind(size)]

    # 5. A.heap-size = A.heap-size - 1
    size -= 1

    # 6. MAX-HEAPIFY(A,1,SIZE)
    A = heap1.maxHeapify(A, 1, size)

    # 7. return max
    return maxElement
