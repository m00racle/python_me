### this will simulate the fibonacci rabgbit growth but with modification
## the input signal x(n) instead of 1,0,0,0,... now will be 1,1,1,....
## in other word each month there will be 1 children pair immigrated into the system

def f(n):
    #base case
    if n == 0 : 
        return 1
    elif n < 2 :
        # first special recursive case
        return f(n-1) + 1
    else:
        #recursive case
        return f(n-1) + f(n-2) + 1

# let's test run the code
for i in range(20):
    print(f(i))
