# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:30:49 2020

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


def dct_split(img_in):    
    
    m,n = img_in.shape

    col_right, col_left = padding_param(m)
    row_bottom, row_top = padding_param(n)
    
    img = np.zeros([m+row_top+row_bottom,n+col_left+col_right])
    img[row_top:m+row_top, col_left:n+col_left] = img_in.copy()
    
    out_img = np.zeros(img.shape)
    
    for i in range(0,int(len(img)/8)):
        for j in range(0,int(len(img[i])/8)):
            
            temp = img[8 * i: 8*i+8, 8*j: 8*j+8]
            
            temp = np.float32(temp)
            temp = cv2.dct(temp)
            
            out_img[8*i: 8*i+8, 8*j: 8*j+8] = temp
    
    return out_img