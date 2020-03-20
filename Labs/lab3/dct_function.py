# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:25:25 2020

@author: Michael Hage
"""


import numpy as np
import cv2

def padding_param(a):
    
    if a % 2 == 1:
        
        b  =  8 - (a % 8)
        
        n = int((b - 1)/ 2)
        m = int(n + 1)
    
    else:
        b = 8 - (a % 8)
        
        n = int(b / 2)
        m = int(n)
    
    return m,n

def idct_split(img):
    
    img_out = np.zeros(img.shape)
    
    for i in range(0,int(len(img)/8)):
        for j in range(0,int(len(img[i])/8)):
            temp = img[8 * i: 8*i+8, 8*j: 8*j+8]
            
            temp = cv2.idct(temp)
            
            img_out[8*i: 8*i+8, 8*j: 8*j+8] = temp
    
    return np.uint8(img_out)


def dct_split(img_in):    
    
    m,n = img_in.shape

    col_right, col_left = padding_param(n)
    row_bottom, row_top = padding_param(m)
    
    img = np.zeros([m+row_top+row_bottom,n+col_left+col_right])
    img[row_top:m+row_top, col_left:n+col_left] = img_in.copy()
    
    img_out = np.zeros(img.shape)
    
    for i in range(0,int(len(img)/8)):
        for j in range(0,int(len(img[i])/8)):
            
            temp = img[8 * i: 8*i+8, 8*j: 8*j+8]
            
            temp = np.float32(temp)
            temp = cv2.dct(temp)
            
            img_out[8*i: 8*i+8, 8*j: 8*j+8] = temp
    
    return np.float32(img_out)


def quantization(img_in, n):
    
    img = img_in.copy()
    img_out = np.zeros(img.shape)
    
    stepsize = []
    for i in range(0,int(len(img)/8)):
        for j in range(0,int(len(img[i])/8)):
            
            temp = img[8 * i: 8*i+8, 8*j: 8*j+8]
            
            v_max = np.amax(temp)
            v_min = np.amin(temp)
            
            q = (v_max - v_min) / 2**n
            # print(q)
            
            temp = np.round(temp / q)
            
            stepsize.append(q)
            img_out[8*i: 8*i+8, 8*j: 8*j+8] = temp
    
    x = 0
    for i in range(0,int(len(img)/8)):
        for j in range(0,int(len(img[i])/8)):
            
            img_out[8 * i: 8*i+8, 8*j: 8*j+8] *= stepsize[x]
            
            x += 1
            
    return np.float32(img_out)                