def add_norm(a, b):
    """ 
    parameters a:int, b:int

    this is return addition of a + b

    return int
     """
    return a + b

def add_inf(a, b, *, norm=0, press=5):
    return a + b - norm + press

def add_min(a, b, norm=3, press = 0):
    return a + b - norm


if __name__ == '__main__':
    print(add_norm(3, 4))
    print(add_inf(2,3, press = 4, norm=5))
    print(add_min(3,5))
    print(add_min(37, 5, 34))
    print(add_norm(b=3, a=10))
