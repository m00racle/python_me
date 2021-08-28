def ind(i):
    """
    convert index (starts from 1) to Python index (starts from 0)
    param:
    i (int) = index

    return: int
    """
    return i-1

def partition(A, p, r):
    """
    process the partition in the quick sort function.
    param: 
    A (array) = list of numbers, p (int) = index in the list, r (int)=index in the list (p < r)
    
    return: array
    """
    x = A[ind(r)]
    i = p - 1
    # loop from p to r-1 (inclusive)
    for j in range(p, r):
        if A[ind(j)] <= x:
            i += 1
            temp = A[ind(i)]
            A[ind(i)] = A[ind(j)]
            A[ind(j)] = temp
    
    temp2 = A[ind(i + 1)]
    A[ind(i + 1)] = A[ind(r)]
    A[ind(r)] = temp2
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