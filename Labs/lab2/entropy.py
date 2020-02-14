# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:48:58 2020

@author: Michael
"""
import numpy as np
import matplotlib.pyplot as plt
    
# Calculate the historgram and the Entropy of a given dataset
def myEntropy(X):
    
    arr = X.copy()
    
    arr = np.ravel(arr)
    
    stats = {}
    for i in arr:
        if i in stats:
            stats[i] += 1
        else:
            stats[i] = 1
        
    values = np.array(list(stats.values())) 
    
    values = values / sum(values)
    
    entropy = -sum(values * np.log2(values))
    
    return [stats,entropy]