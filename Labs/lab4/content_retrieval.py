# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:26:18 2020

@author: Michael Hage
"""


import cv2
import numpy as np
import display_functions as df

def hashmap(X, bins=0):
    
    if(not isinstance(X, str)):
        arr = X.copy()
        arr = np.ravel(arr)
    else:
        arr = X
    
    stats = {}
    
    # sets predetermined bins
    if bins!=0:
        for i in range(0,bins):
            stats[i] = 0
    
    for i in arr:
        if i in stats:
            stats[i] += 1
        
        else:
            stats[i] = 0
    return stats

def histogram_bin(img, bins, title, d):
    
    
    descriptors = [": H ", ": S ", ": V "]
    
    step=[]
    arr = []
    
    for i in range(0,len(bins)):
        max_val = np.iinfo(img.dtype).max
        min_val = np.iinfo(img.dtype).min
        
        # create bin step size
        step = (max_val - min_val + 1) / bins[i]
        
        # finds which bin the item belongs to
        group = np.array(np.floor(img[:,:,i] / step), dtype=np.int)
        
        # multiply bin by step size to find range
        # group = group[:,:] * step
        
        # create hashmap to make histogram
        his = hashmap(group, bins[i])
        
        if d == 1:
            # display histogram
            df.histogram(his, title = title + descriptors[i] + "Channel")
        
        # create array to sort by bin step value
        n = np.array(list(his.items()))
        n = n[n[:,0].argsort(kind='mergesort')]
        
        # append hashmap to output list
        arr.append(n)  
        
    return arr

def manhattan_distance(query, match):
    
    d_sum = 0
    
    for i in range(0,len(query)):
        q = query[i]
        m = match[i]
        
        d_sum += sum( abs(q[:,1] - m[:,1]) )
        
    return d_sum

def euclidian_distance(query, match):
    
    # prevent overflow
    scale = 1000
    d_sum = 0
    
    for i in range(0,len(query)):
        q = query[i]
        m = match[i]
        
        d_sum += sum( np.sqrt((q[:,1] - m[:,1])**2 )) / scale
        
    return d_sum

def histogram_intersection(query, match):
    
    d_sum = 0
    
    for i in range(0,len(query)):
        min_bins = min([len(query[i]), len(match[i])])
        
        q = query[i]
        m = match[i]
    
        
        d_sum += sum( np.minimum( q[:,1], m[:,1] ) ) / min_bins
    
    return d_sum