def parent(i):
    return i//2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def ind(i):
    if i > 0:
        return i - 1
    else:
        return None

def maxHeapify(A, i):
    # l = LEFT(i)
    l = left(i)
    # r = RIGHT(i)
    r = right(i)
    # if l <= A.heap-size and A[l] > A[i]
    if l <= len(A) and A[ind(l)] > A[ind(i)]:
        #   largest = l
        largest = l
    # else largest = i
    else: largest = i

    # if r <= A.heap-size and A[r] > A[largest]
    if r <= len(A) and A[ind(r)] > A[ind(largest)]:
        #   largest = r
        largest = r
    
    # if largest != i 
    if largest != i:
        #   exchange A[i] with A[largest]
        switch = A[ind(i)]
        A[ind(i)] = A[ind(largest)]
        A[ind(largest)] = switch
    #   maxHeapify(A, largest)
    return None

