import os, sys, math
from unittest.main import main
module_path = os.path.normpath(os.path.dirname(__file__) + "/../../modules")
sys.path.append(module_path)

from idx import idx
import numpy as np
from time import perf_counter, perf_counter_ns

def find_max_cross_subarray(A, low, mid, high) -> tuple :
    """
    finding maximum sum of values as subarray 
    but crossing the subarray
    return tuple (max_left (int), max_right (int), left_sum + right_sum (number))

    Parameter:
    A : array like of number
    low : first component index in the array A starting from 1 (int) 
    mid : middle component index in the array A starting from 1 (int)
    high: last component index in the array A starting from 1 (int)
    maxVal: (default True) true means seek for maximum sum false means minimum sum (boolean)
    """
    left_sum = -math.inf
    sum = 0
    for i in range(mid, 0, -1):
        # BUG RESOLVED: the lower limit is set to 0 instead of 1 since it is mid <= i < 0 thus 0 will be omitted!
        sum = sum + A[idx(i)]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    # for the right side
    right_sum = -math.inf
    sum = 0
    for j in range(mid + 1, high+1):
        sum = sum + A[idx(j)]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    
    return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(A, low, high):
    """
    find max subarray of delta values.
    return: tuple(low (int), high (int), sum (int))

    parameters: 
    A : array like of numbers (List)
    low : index of lowest position in array to be inspected (int)
    high : index of highest position in array to be inspected (int)
    """
    if high == low:
        return (low, high, A[idx(low)])
    else:
        mid = (low + high) // 2
        # the recursion is not merging but COMBINATION: the low and high parameters passed is constant!
        (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_cross_subarray(A, low, mid, high)
        # choose which to return
        if left_sum >= right_sum and left_sum >= cross_sum :
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else: return (cross_low, cross_high, cross_sum)

def brute_max_subarray(A, low, high):
    """
    find max sub-array using brute force method.
    return: tuple(low (int), high (int), sum (int))

    parameters: 
    A : array like of numbers (List)
    """
    max_sum = -math.inf
    for i in range(low, high + 1): 
        # since this is exclude the high thus the top limit should high + 1
        sum = 0
        for j in range(i, high + 1):
            # the i as starting point is because there is the max value in the same low, and high index
            sum += A[idx(j)]
            if sum > max_sum:
                max_sum = sum
                max_left = i
                max_right = j

    return (max_left, max_right, max_sum)

def iterative_max_subarray(A, low, high):
    """
    finding max sub array using iterative method
    return tuple (low (int), high (int), sum (int))

    parameters:
    A : array of numbers
    low : lowest start index starts from 1 (int)
    high : highest end index starts from 1 (int)
    """
    max_sum = -math.inf
    sum = 0
    for j in range(low, high + 1):
        current_right = j
        if sum > 0:
            sum += A[idx(j)]
        else:
            current_left = j
            sum = A[idx(j)]
        # now register each current sub array
        if sum > max_sum:
            max_sum = sum
            max_left = current_left
            max_right = current_right

    return (max_left, max_right, max_sum)

def main():
    """
    main run
    """
    np.random.seed(10)

    brute_time = -math.inf
    div_time = math.inf
    n = 10
    while brute_time < div_time:
        A = np.random.randint(-10,5, n)
        # find max using brute force
        start_time = perf_counter()
        brute_result= brute_max_subarray(A, 1, len(A))
        end_time = perf_counter()
        brute_time = end_time - start_time

        # find max using divide and conquer
        start_time = perf_counter()
        div_result = find_max_subarray(A, 1, len(A))
        end_time = perf_counter()
        div_time = end_time - start_time
        
        n += 10
    # print the report
    print(f"number of samples: {n}")
    print(f"runnig time brute force: {brute_time}")
    print(f'brute force: {brute_result}')
    print(f"runnig time div-conquer: {div_time}")
    print(f'divide and conquer: {div_result}')


if __name__ == "__main__":
    main()