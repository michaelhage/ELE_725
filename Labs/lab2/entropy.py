# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:48:58 2020

@author: Michael
"""

import numpy as np
import pandas as pd

# Calculate the historgram and the Entropy of a given dataset
def myEntropy(X):
    
    stats = {}
    for i in X:
        if i in stats:
            stats[i] += 1
        else:
            stats[i] = 1
        
    values = np.array(list(stats.values())) 
    
    return stats

    