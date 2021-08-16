import heap1

ind = heap1.ind

def heapMax(A):
    return A[ind(1)]

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
    maxElement = A[ind(1)]

    # 4. A[1] = A[A.heap-size]
    A[ind(1)] = A[ind(size)]

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
    if key < A[ind(i)]: raise ValueError("new key is smaller than current element value")

    # 3. A[i] = key
    A[ind(i)] = key

    # 5. while i > 1 and A[PARENT(i)] < A[i]:
    while i > 1 and A[ind(heap1.parent(i))] < A[ind(i)]:
        # 6. exchange A[PARENT(i)] with A[i]
        temp = A[ind(heap1.parent(i))]
        A[ind(heap1.parent(i))] = A[ind(i)]
        A[ind(i)] = temp

        # i = parent(i)
        i = heap1.parent(i)

    return A