# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:45:49 2020

@author: Michael
"""
import cv2
import numpy as np
import pandas as pd
import entropy as en
import display_functions as df
import huffman

# Colored Image
img1 = cv2.imread("MikeySpiece.png", 1)
df.display_image(img1, 'Self Portrait')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)

img1_dict_Cr, img1_ent_Cr = en.myEntropy(img1[1])
img1_dict_Cb, img1_ent_Cb = en.myEntropy(img1[2])

print("Entropy Cr Channel: "+ str(img1_ent_Cr))
print("Entropy Cr Channel: "+ str(img1_ent_Cb))

df.histogram(img1_dict_Cr)
df.histogram(img1_dict_Cb)

# Grayscale Image
img2 = cv2.imread("bridge.jpg", 0)
df.display_image(img2)

img2_dict, img2_ent = en.myEntropy(img2)

df.histogram(img2_dict)

print("Entropy Channel: "+ str(img2_ent))

# Huffman Encoding