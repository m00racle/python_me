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

def fruit_basket(*ordering, **kwargs) -> int:
    orders = 0
    for num in ordering: orders += num
    print("number of orders: ", orders)

    # basket_list = ["orange", "apple", "strawberry", "pineapple"]
    basket_price = {
        "orange" : 500,
        "apple" : 750,
        "strawberry" : 250,
        "pineapple" : 300
    }
    total = 0
    # test the key available in the basket_list
    for key in kwargs:
        if key in list(basket_price.keys()) : 
            subtotal = kwargs[key] * basket_price[key]
            print(key, '->', kwargs[key], ' x ', basket_price[key], ' = ', subtotal)
            total += subtotal
        else :
            print(key, '-> Not available')
    
    print("the total cost for all order: ", total , " x ", orders)
    return total * orders

if __name__ == '__main__':
    # print(add_norm(3, 4))
    # print(add_inf(2,3, press = 4, norm=5))
    # print(add_min(3,5))
    # print(add_min(37, 5, 34))
    # print(add_norm(b=3, a=10))
    cost = fruit_basket(4, 6, 1, orange=5, apple=3, blackberry=5, pineapple=7)
    print("my total basket cost= ", cost)