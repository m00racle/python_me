def f(n):
    ## this is fibonacci rabbit equation
    # base case 
    if n <2:
        return 1
    else:
        #recursive case
        return f(n-1) + f(n-2)

# now we test the equation:
for i in range(20):
    print(f(i))
