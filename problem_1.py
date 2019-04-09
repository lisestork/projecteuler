#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:43:43 2019

@author: lisestork
"""

#Problem 1: 
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000

import time
import numpy as np

start = time.time()
all_ints = np.linspace(0,999,1000, dtype=int)
answer = sum(all_ints[(all_ints % 3 == 0) + (all_ints % 5 == 0)])
end = time.time()
print("Script ran for {} seconds".format(end-start))
print(answer)