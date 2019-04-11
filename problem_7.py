#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:57:42 2019

@author: lisestork
"""

#problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

import time 

def next_prime(n):  
    for i in range(n+1, 2*n):
        if([j for j in range(1,i) if (i % j == 0)] == [1]):
            return i
            break
            
def ith_prime(n):
    i = 2
    for idx in range(2,n+1):
        i = next_prime(i)
    return i

start = time.time()
x = ith_prime(10001)    
end = time.time()
print("Script ran for {} seconds".format(end-start))
print("Answer: ", x)

