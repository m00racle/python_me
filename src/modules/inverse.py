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
    return pulv.gcd(n,a).t