#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:02:12 2019

@author: lisestork
"""
import numpy as np
from math import gcd
import time

#problem 5_2: 
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def lcm(a):
    b = a[0]
    for i in a[1:]:
      b = int(b*i/gcd(b, i))
    return b

a = sorted(np.arange(1,21))
start = time.time()
x = lcm(a)
end = time.time()
print("Script ran for {} seconds".format(end-start))
print("Answer: ", x)
