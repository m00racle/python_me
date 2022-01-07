class LinearCombination(object):
    def __init__(self, value:int, s:int, t:int) -> None:
        self.value = value
        self.s = s
        self.t = t

def extGcd(x:LinearCombination, y:LinearCombination) -> LinearCombination:
    if (y.value == 0):
        return x
    
    q:int = x.value // y.value
    s:int = x.s - q * y.s
    t:int = x.t - q *y.t

    remains = LinearCombination(x.value - q*y.value, s, t)

    # begin recursive steps
    return extGcd(y, remains)

def gcd(a:int, b:int):
    # the initial condition for the GCD and pulverizer steps
    if (a==0 and b == 0 ):
        return LinearCombination(-1,0,0)
    
    if (a == 0):
        # the gcd is b
        return LinearCombination(b, 0, 1)
    
    x:LinearCombination = LinearCombination(a, 1, 0)
    y:LinearCombination = LinearCombination(b, 0, 1)

    # start recursive steps
    return extGcd(x, y)

