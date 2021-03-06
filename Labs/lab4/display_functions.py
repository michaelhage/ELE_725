# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:39:15 2020

@author: Michael
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import cv2

def histogram(dictionary, spacing = 1, title="Image Histogram"):
    plt.bar(dictionary.keys(), dictionary.values(), spacing, color='b')
    plt.title(title)
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
    
def plot(X):
    fig, ax = plt.subplots()
    
    ax.plot( np.arange(1,len(X)+1), X)
    ax.set(xlabel='Frame Difference', ylabel='Entropy')
    ax.grid()
    
    plt.show()