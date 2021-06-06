"""
algorithms.py
Prime number generation algorithms
@author: Dan Batiste
"""

import random as rand
from math import *
import time
import numpy as np

# Prime checker
def is_prime(n):
    """Checks all possible factors up to floor(sqrt(n))"""
    if n == 2:
        return True
    upperbound = sqrt(n)//1
    x = 2
    while n % x != 0 and not x == n and not x > upperbound:
        if x == 2:
            x += 1 # x is 2
            continue
        x += 2 # x is odd
    if x > upperbound:
        return True
    return False
        

# Naive algorithm
def naive_algorithm(start, end):
    return [x for x in range(start, end+1) if is_prime(x)]

## Sieves

""" DEPRACATED
def sieve_of_eratosthenes(start, end):
    # Starts at 1 but only returns from `start` to `end`
    sieve = list(range(1, end+1)) # interval [start, end] (inclusive)
    # I only need to check up to floor(sqrt(end))
    upperbound = int(sqrt(end)//1)
    for x in range(1, upperbound): 
        if x == 1: # If the sieve filtering starts at 1, all numbers will be filtered out.
            continue
        sieve = [s for s in sieve if (not s%x == 0) or (s == x)]
    return list(filter(lambda x: x >= start, sieve))
"""
def sieve_of_eratosthenes(start, n):
     # Source: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    results = []
    for p in range(2, n+1):
        if prime[p] and p >= start:
            results.append(p)
    return results



def sieve_of_sundaram(start, n):
    # Taken from https://en.wikipedia.org/wiki/Sieve_of_Sundaram
    # Half written by me
    k = (n - 2) // 2
    integers_list = [True] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            integers_list[i + j + 2 * i * j] = False
            j += 1
    """
    if n > 2:
        print(2, end=' ')
    for i in range(1, k + 1):
        if integers_list[i]:
            print(2 * i + 1, end=' ')
    """
    check = lambda i, b: b and (i > 0) and ((2*i + 1) >= start)
    if n > 2:
        integers_final = [2*i + 1 for i, b in enumerate(integers_list) if check(i, b)]
        if start <= 2:
            integers_final.insert(0,2)
        return integers_final
    
    return [2*i + 1 for i, b in enumerate(integers_list) if check(i, b)]