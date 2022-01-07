from unittest import result
import pulverizer as pulv

"""
This is the lib to find inverse of certain mod (if exist)
"""

def inverseOf(a:int, n:int):
    """
    find the inverse of a in the ring of Z base n
    (in mod n)
    a:int = number which inverse is in question
    n:int = mod (ring of Z) base 
    """
    if pulv.gcd(n,a).value != 1 :
        raise ValueError("the number is not relatively prime to the mod base!")
    else:
        result = pulv.gcd(n,a).t
        while result <= 0:
            # keep adding base n until the inverse result is positive
            result += n
        
        return result