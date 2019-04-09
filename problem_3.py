#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:27:12 2019

@author: lisestork
"""

#problem 3: 
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

def next_prime(n):
    
    for i in range(n+1, 2*n):
        if([j for j in range(1,i) if (i % j == 0)] == [1]):
            return i
            break

def prime_factors(n,primes=[2]):
    factors = []
    while n != 1:
        if(n % primes[-1] == 0):
            #if divisible by prime, divide by prime
            factors.append(primes[-1])
            n = n / primes[-1] 
        else: 
            #else, find next smallest prime
            primes.append(next_prime(primes[-1]))
    return max(factors)
    
import time

start = time.time()
x = prime_factors(600851475143)
end = time.time()
print("Script ran for {} seconds".format(end-start))
print("Answer: ", x)