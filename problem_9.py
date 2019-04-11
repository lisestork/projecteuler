#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:15:20 2019

@author: lisestork
"""
#Problem 9:
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^2 + b^2 = c^2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import numpy as np
import time

def pyth_triplet(s, found=False):

    while not found:
        n = np.random.randint(2,np.sqrt(s))
        m = np.random.randint(1,n)
        a = n**2 - m**2
        b = 2*n*m
        c = n**2 + m**2
        if(a + b + c == s):
            return a*b*c
            found = True
    
start = time.time()
x = pyth_triplet(1000)
end = time.time()
print("Script ran for {} seconds".format(end-start))
print("Answer: ", x)        