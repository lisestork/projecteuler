#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:17:54 2019

@author: lisestork
"""

#problem 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
import numpy as np
import time

def sum_primes_below(n):
    a = np.arange(2,n)
    p = []
    
    while len(a) > 0:
            p.append(a[0])
            idx = np.nonzero(a % a[0])
            a = a[idx]            
    return sum(p)

start = time.time()
x = sum_primes_below(2000000)
end = time.time()
print("Script ran for {} seconds".format(end-start))
print("Answer: ", x)  
    