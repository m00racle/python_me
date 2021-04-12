# this is the python code for the 6-003 homework 1

import math
from pylab import * #this is part of matplot lib used to create graphs
import numpy as np
import matplotlib.pyplot as plt

# We begin the data using analytical method:
#prepare empty list
ya = []
for t in range(60):
    ya.append(0.1 - 0.1 * math.e**(-t/20.0))
print (ya)
plt.plot(range(60),ya,'r-')

# Now we go numerical
# let's put the variables first:
T = 1 #seconds

# since in numerical version we use time steps we need to calculate based on the previous value
# given initial condition of r1 at t=0 is = then we put that value first in the list
yn = [0] #a list with r1[0] = 0
for n in range(1,60):
    yn.append(yn[n-1] + T/20 * (0.1 - yn[n-1]))
print
print ('numeric list', yn)

# now we need to present the graphical comparison between the analytic and numeric
plt.stem(range(60), yn, ":")
plt.show()

# now we calculate the max difference between numeric and analytic methods
print
print('biggest difference: ', max(abs(ya[i]-yn[i]) for i in range(60)))
