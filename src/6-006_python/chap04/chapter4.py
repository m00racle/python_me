import os, sys, math
from unittest.main import main
module_path = os.path.normpath(os.path.dirname(__file__) + "/../../modules")
sys.path.append(module_path)

from idx import idx

def find_max_cross_subarray(A, low, mid, high) -> tuple :
    """
    finding maximum sum of values as subarray 
    but crossing the subarray
    return tuple (max_left (int), max_right (int), left_sum + right_sum (number))

    Parameter:
    A : array like of number
    low : first component index in the array A (int)
    mid : middle component index in the array A (int)
    high: last component index in the array A (int)
    maxVal: (default True) true means seek for maximum sum false means minimum sum (boolean)
    """
    left_sum = -math.inf
    sum = 0
    for i in range(mid-1, 0, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    # for the right side
    right_sum = -math.inf
    sum = 0
    for j in range(mid, high):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    
    return (max_left, max_right, left_sum + right_sum)
    