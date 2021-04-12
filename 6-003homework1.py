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
plt.show()