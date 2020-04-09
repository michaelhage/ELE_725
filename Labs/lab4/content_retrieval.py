# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:26:18 2020

@author: Michael Hage
"""


import cv2
import numpy as np
import display_functions as df

def hashmap(X):
    
    if(not isinstance(X, str)):
        arr = X.copy()
        arr = np.ravel(arr)
    else:
        arr = X
    
    stats = {}
    for i in arr:
        if i in stats:
            stats[i] += 1
        else:
            stats[i] = 1
            
    return stats

def histogram_bin(img, bins, title, d):
    
    descriptors = [": H ", ": S ", ": V "]
    
    step=[]
    arr = []
    
    for i in range(0,len(bins)):
        max_val = np.amax(img[i])
        min_val = np.amin(img[i])
        
        # create bin step size
        step = (max_val - min_val) / bins[i]
        
        # finds which bin the item belongs to
        group = np.array(np.floor(img[i] / step), dtype=np.int)
        
        # multiply bin by step size to find range
        group = group[:,:] * step
        
        # create hashmap to make histogram
        his = hashmap(group)
        
        if d == 1:
            # display histogram
            df.histogram(his, title = title + descriptors[i] + "Channel")
        
        # create array to sort by bin step value
        n = np.array(list(his.items()))
        n = n[n[:,0].argsort(kind='mergesort')]
        
        # append hashmap to output list
        arr.append(n)  
        
    return arr