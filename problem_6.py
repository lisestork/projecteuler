#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:36:40 2019

@author: lisestork
"""


#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import numpy as np 
import time
# Sum of the squares of the first one hundred natural numbers:

def diff(n):
    return abs((np.sum([x**2 for x in range(1,n+1)])) - (np.sum([x for x in range(1,n+1)])**2))

start = time.time()
x = diff(100)
end = time.time()
print("Script ran for {} seconds".format(end-start))
print("Answer: ", x)