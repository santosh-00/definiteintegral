# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 03:43:36 2024

@author: Santosh
"""

import numpy as np

def function(x):
    return 16 * ( x ** 4)
#expected integral is (16/5)x^5 on 0 to 2 which is 102.4

# using monte carlo
x = np.random.uniform(0, 2, 100000)
y = function(x)
moca = (np.sum(y) * (2 - 0)) / 100000
print("integral approximation using monte carlo is " + str(moca))

# using reimann sum

dx = (2 - 0)/100000
f_x_sum = 0
for i in range (100001):
    f_x_sum += function(0 + ((i -1) * dx)) * dx

print("integral approximation using reimann sum is " + str(f_x_sum))
    


