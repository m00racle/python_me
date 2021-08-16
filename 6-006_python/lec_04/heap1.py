def parent(i):
    """
    finding the parent of element i
    parameter: i (int) : the current element index
    """
    return i//2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def ind(i):
    """
    return indexing (start from 0)
    converting the pseudo code's indexing which starts from 1
    parameter: i (int) : the pseudo-code index
    """
    if i > 0:
        return i - 1
    else:
        raise ValueError("the i key index reached 0")

def maxHeapify(A, i, size):
    # l = LEFT(i)
    l = left(i)
    # r = RIGHT(i)
    r = right(i)
    # if l <= A.heap-size and A[l] > A[i]
    if l <= size and A[ind(l)] > A[ind(i)]:
        #   largest = l
        largest = l
    # else largest = i
    else: largest = i

    # if r <= A.heap-size and A[r] > A[largest]
    if r <= size and A[ind(r)] > A[ind(largest)]:
        #   largest = r
        largest = r
    
    # if largest != i 
    if largest != i:
        #   exchange A[i] with A[largest]
        switch = A[ind(i)]
        A[ind(i)] = A[ind(largest)]
        A[ind(largest)] = switch
        return maxHeapify(A, largest, size)
    #   maxHeapify(A, largest)
    else: 
        return A

def minHeapify(A, i, size):
    # same as maxHeapify but this time it is minimum heap properties
    # l = LEFT(i)
    l = left(i)
    # r = RIGHT(i)
    r = right(i)
    # if l <= A.heap-size and A[l] < A[i]
    if l <= size and A[ind(l)] < A[ind(i)]:
        #   smallest = l
        smallest = l
    # else smallest = i
    else: smallest = i

    # if r <= A.heap-size and A[r] < A[smallest]
    if r <= size and A[ind(r)] < A[ind(smallest)]:
        #   smallest = r
        smallest = r
    
    # if smallest != i 
    if smallest != i:
        #   exchange A[i] with A[smallest]
        switch = A[ind(i)]
        A[ind(i)] = A[ind(smallest)]
        A[ind(smallest)] = switch
        return minHeapify(A, smallest, size)
    #   maxHeapify(A, smallest)
    else: 
        return A

def maxLoopHeapify(A, i, size):
    # prepare while left(i) loop
    while (left(i) <= size):
        # l = left(i)
        l = left(i)
        # r = right(i)
        r = right(i)
        
        # if A[l] > A[i] then
        if A[ind(l)] > A[ind(i)]:
            # largest = l
            largest = l
        # else largest = i
        else: largest = i

        # if A[r] > A[i] then
        if r <= size and A[ind(r)] > A[ind(largest)]:
            # largest = r
            largest = r
        # if the largest is i then break for the loop return A
        if largest == i: break
        
        # exchange A[i] with A[largest]
        switch = A[ind(i)]
        A[ind(i)] = A[ind(largest)]
        A[ind(largest)] = switch
        # then i = largest to next node
        i = largest
    return A

def buildMaxHeap(A, size):
    # A.heap-size = len(A)
    # for i = lenA//2 (floor division) to 1
    for i in range(len(A)//2, 0, -1):
        # Max-heapafy(A, i)
        A = maxHeapify(A, i, size)
    return A

def heapsort(A):
    # BUILD-MAX-HEAP(A)
    size = len(A)
    A = buildMaxHeap(A, size)
    # for i = len(A) down to 2
    for i in range(len(A), 1, -1):
        # exchange A[1] with A[i]
        temp = A[ind(1)]
        A[ind(1)] = A[ind(i)]
        A[ind(i)] = temp
        # A.heap0size = A.heap-size -1
        size -= 1
        # MAX-HEAPIFY(A,1)
        A = maxHeapify(A, 1, size)

    return A
