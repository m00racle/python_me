# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 09:16:30 2020

@author: m00racle
"""

def recurFibo(n):
    """
    Parameters
    ----------
    n : positive integers (int>0 or natural numbers)
        the order of the fibonacci number calculation

    Returns
    -------
    the final result of the fibonacci sum operation using recursive method

    """
    
    #make sure that n is positive otherwise it will create invinite loop
    if n < 0:
        raise RuntimeError("sorry, only positive integers allowed")
    
      
    # let's start with the Fibonacci 
    # the base case if n is 0 or n is 1, then
    # return 1
    if n == 1 or n == 0:
        return 1
    # else then return recursively (n-1)+(n-2)
    else:
        return recurFibo(n-1) + recurFibo(n-2)
    ### end of def recurFibo(n)
    
def memoFibo(n, memo={}):
    """
    doing Fibonacci sum operation but with memo hash map to speed things up for the larger numbers

    Parameters
    ----------
    n : TYPE positive int or natural numbers
        DESCRIPTION. the order of the fibonaccy
    memo : TYPE dictioanry of int:int, optional
        DESCRIPTION. this dictionary with key is (int) orde of fobonacci and the value is the result of the fibonacci operartion of the key orde. This will kept record of the previous operations and make it a hash map.
        The default is {}.

    Returns
    -------
    the final result of the fibonacci sum operation using recursive method

    """
    # test if the n input is positive
    if n < 0:
        # if not the raise runtime error to stop the process to prevent infinite loop
        raise RuntimeError("sorry, only positive integers allowed")
    
    # set base case if n is 1 or n is 0 then return 1
    if n == 1 or n==0:
        return 1
    # if not then check in the memo dictionary whether the operation has been done before or not
    # if yes return the result from the dictionary directly
    try:
        return memo[n]
    # if not then make recursive call for memoFibo(n-1)+memoFibo(n-2)
    except (KeyError):
        # NOTE: if the error is not found int he memo dictionary from the try part above then the python will give KeyError exception. this is th part we handle that exception
        result = memoFibo(n-1, memo) + memoFibo(n-2,memo)
        # NOTE: we take the memo with us to try to see if the n-1 and/or n-2 is already part of our step in finding the result of the fibonacci. If yes it should just return that previous results
        # the result of that recursion then saved into the memo dictionary with the key is n
        memo[n] = result
        # return the result 
        return result
    
    ### end of def memoFibo(n, memo={}):