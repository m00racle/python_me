from logging import raiseExceptions
import os, sys, math
module_path = os.path.normpath(os.path.dirname(__file__) + "/../../modules")
sys.path.append(module_path)

from idx import idx

def matrix_product(A,B):
    """
    find product of matrix A and B multiplication.
    return : List of List of numbers

    Parameters:
    A = List of List number represent matrix n x m 
    B = List of List number represent matrix n x m
    """
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])
    # C = A.B
    C = []
    
    for i in range(rowA):
        # assert matrix error
        if len(A[i]) != len(B): raise Exception("matrix shape mismatch")
        C.append([])
        for j in range(len(B[i])):
            C[i].append(0)
            for k in range(rowB):
                # assert matrix error
                if len(B[k]) != len(B[i]) : raise Exception("matrix B shape non symetric")
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C