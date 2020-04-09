# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 02:55:50 2020

@author: Michael Hage
"""

import cv2
import numpy as np

# padding function
def padding_param(a, win):
    
    if a % 2 == 1:
        
        b  =  win - (a % win)
        
        n = int((b - 1)/ 2)
        m = int(n + 1)
    
    else:
        b = win - (a % win)
        
        n = int(b / 2)
        m = int(n)
    
    return m,n


# divide blocks into 16 x 16 blocks
def image_divide(X, win):
    
    img = X.copy()
    
    [a,b] = img.shape
    
    [left,right] = padding_param(b, win)
    [top,bottom] = padding_param(a, win)
    
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT)
    
    [a,b] = img.shape
    
    out_img = np.zeros( [np.int((a * b) / win**2), win, win], dtype=np.uint8)
    
    x = 0
    
    for i in range(0,np.int(a/16)):
        for j in range(0,np.int(b/16)):
            
            out_img[x,:,:] = img[i*win:i*win+win, j*win:j*win+win]
            x += 1
    return out_img
   
# computing motion vectors for nxn blocks in a k radius
# used Sum of Absolute Difference instead of Mean Absolute Difference
def computeMotionVector(framePrev, f, p, q, k, win):
    
    
    X = np.array(framePrev.copy(), dtype = np.int)
    
    sentinel = np.iinfo(np.int).max - 1
    bound_x,bound_y = framePrev.shape
    
    sad = np.ones([2 * k + 1, 2 * k + 1], dtype=np.int) * sentinel
    
    for i in range(-k, k+1):
        for j in range(-k,k+1):
            
            if (p+i > 0) and (q+j > 0) and (p+win+i < bound_x) and (q+win+j < bound_y):
                
                # print(X[p+i : p+i+win, q+j : q+j+win].shape)
                sad[i+k,j+k] = np.sum( abs( X[p+i : p+i+win, q+j : q+j+win] - f[:,:] ) )
                
    index = np.unravel_index(sad.argmin(), sad.shape)
    # print(index)
    
    return np.array(index[:]) - k

# DPCM based on motion vectors
def DPCM_encoder_frame(frame, mv, win):
    
    a,b = frame.shape
    x = 0

    dpcm = np.zeros([a,b], dtype = np.int)
    
    for i in range(0,np.int(a/win)):
        for j in range(0,np.int(b/win)):
            
            x1 = np.int(win*i)
            x2 = np.int(x1 + mv[x,0])
            y1 = np.int(win*j)
            y2 = np.int(y1 + mv[x,1])
            
            temp = frame[x1:x1+win, y1:y1+win] - frame[x2:x2+win, y2:y2+win]
            
            dpcm[x1:x1+win, y2:y2+win] = temp
            x += 1
            
    return dpcm

# DPCM encoder based on the previous frame
def DPCM_encoder(frame_prev, frame_next):
    
    dpcm = np.zeros_like(frame_prev)
    
    for i in range(0,len(frame_prev)):
        for j in range(0,len(frame_prev[i])):
            
            dpcm[i,j] = frame_prev[i,j] - frame_next[i,j]
            
    return dpcm