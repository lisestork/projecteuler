#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:00:20 2019

@author: lisestork
"""
#
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

import numpy as np
import itertools
import time

def palindrome(digits):
      
    a = np.arange(pow(10,digits-1),pow(10,digits),1,dtype=int)
    p = list([x * y for x, y in itertools.product(a, a)])
    for nr in sorted(p, reverse=True): 
        if(nr == reversed(nr)):
            return nr
            break
      
start = time.time()
x = palindrome(3)
end = time.time()
print("Script ran for {} seconds".format(end-start))
print("Answer: ", x)
