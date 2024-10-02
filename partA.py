# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:04:09 2024

@author: Phuong Nguyen
"""
"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
#VERSION 1
from math import sqrt
def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
# Calculating the mean
    N = len(x)
    total_sum = 0
    for i in x:
        total_sum += i
    mean = total_sum / N
 
    
#Calculating the mean of squares
    sum_square = 0
    
    for i in x:
        sum_square += i ** 2
    mean_square = sum_square / N

# Calculating the variance
    variance = mean_square - (mean**2)
    
#Calculating the standard deviation
    sd = sqrt (variance)
    
    return sd

#VERSION 2
def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    N = len (x)
    mean = sum(x) / N
    mean_square = sum(i**2 for i in x) / N
    variance = mean_square - (mean **2)
    sd = sqrt (variance)
    
    return sd

#VERSION 3    
import numpy as np           
def std_numpy(x):
    return np.std(x)

x = [1,2,3,4,5] 

print (f'The standard deviation using for loops is equal to {std_loops(x)} ')
print (f'The standard deviation using built in functions is equal to {std_builtin(x)} ')
print (f'The standard deviation using NumPy is equal to {std_numpy(x)} ')