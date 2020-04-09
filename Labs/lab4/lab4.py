# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:09:37 2020

@author: Michael Hage
"""

import numpy as np
import video_function as vf
import cv2
import display_functions as df
import mv_functions as mvf
import entropy as en
import glob
import content_retrieval as cbr

# Part 1: Motion Vector Computation

gif = "luigi.gif"

# open video file
video = cv2.VideoCapture(gif)
rate = video.get(5)

# extracts frames
f = 2
imgs = vf.frame_extract(video, f)

df.display_multiple_images(imgs)

# image difference
img_dif = imgs[1] - imgs[0]

df.display_image(img_dif)

# divide image into 16x16 blocks
win = 16
frame_div = mvf.image_divide(imgs[1],win)

# padding first frame like the second in the mvf function
[a,b] = imgs[0].shape

[left,right] = mvf.padding_param(b, win)
[top,bottom] = mvf.padding_param(a, win)
    
frame_pad = cv2.copyMakeBorder(imgs[0], top, bottom, left, right, cv2.BORDER_REFLECT)

# parameters for motion vector function
a,b = frame_pad.shape
k = 7
p = 0
q = 0
motion_vector = np.zeros([len(frame_div), 2])

# computing motion vector
for i in range(0,len(frame_div)):
    
    # print(p,q)
    motion_vector[i,:] = mvf.computeMotionVector(frame_pad, frame_div[i,:,:], p, q, k, win)
    
    q += win
    
    if(q == b):
        q = 0
        p += 16

# DPCM encode by motion vectors
frame_DPCM_div = mvf.DPCM_encoder_frame(frame_pad, motion_vector,win)

# crop frame to original size
frame_DPCM_div = frame_DPCM_div[top:top+len(imgs[0]),left:left+len(imgs[0,0])]

# DPCM encode by individual pixels
frame_DPCM_all = mvf.DPCM_encoder(imgs[0], imgs[1])

# calculate entropy
# motion vector

_,mv_entropy = en.myEntropy(frame_DPCM_div)
_,in_entropy = en.myEntropy(frame_DPCM_all)

print("Entropy of motion vector DPCM: " + str(mv_entropy))
print("Entropy of individual DPCM: " + str(in_entropy))

img_coded = np.uint8(imgs[0] + frame_DPCM_div)

df.display_multiple_images([imgs[1], img_coded])

# Part 2: Content Based Retrival

# extract all photos from folder
url = "Images/"
filenames = [img for img in glob.glob(url+"*.jpg")]
img = [cv2.imread(image,1) for image in filenames]

# create histograms
bins = [30, 15, 15]
his=[]

# set display to 1 to display histogram
# display = 1
display = 0

for i in range(0,len(img)):
    
    # extract filename for histogram title
    s = filenames[i]
    s = s[len(url):]
    
    # 
    img_hsv = cv2.cvtColor(img[i], cv2.COLOR_BGR2HSV)
    
    his.append( cbr.histogram_bin(img_hsv, bins, s, display) )