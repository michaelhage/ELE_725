# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:45:49 2020

@author: Michael
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def display(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def display_multiple_images(img):
    for i in range(len(img)):
        cv2.imshow('image ' + str(i + 1), img[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Calculating Entropy

