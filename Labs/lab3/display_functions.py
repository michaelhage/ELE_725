# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:39:15 2020

@author: Michael
"""
import matplotlib.pyplot as plt
import numpy as np
import cv2

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

def histogram(dictionary, spacing = 1):
    plt.bar(dictionary.keys(), dictionary.values(), spacing, color='b')
    plt.show()

def display_image(img, title = "image"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def display_multiple_images(img):
    for i in range(len(img)):
        cv2.imshow('image ' + str(i + 1), img[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def colormap(img):
    
    plt.style.use('classic')
    plt.imshow(img)
    plt.colorbar();
    
    # d = 70
    
    # plt.figure(figsize=(len(img),len(img[0])), dpi=d )
    
    # color_map = plt.imshow(img)
    # color_map.set_cmap("Blues_r")
    
    # plt.colorbar()
    # plt.show()
    
    # plt.savefig("colormap.png")