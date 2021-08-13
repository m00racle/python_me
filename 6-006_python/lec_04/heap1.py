def parent(i):
    return int(i/2)

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

def unitTest():
    assert parent(5) == 2, "should be 2"
    assert left(2) == 4, "should return 4"
    assert right(2) == 5, "should return 5"
    assert ind(1) == 0, "should return zero"
    assert ind(0) == None, "should return None"
    assert ind(5) == 4, 'should return 4'

unitTest()