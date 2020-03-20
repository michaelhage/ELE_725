# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:03:04 2020

@author: Michael Hage
"""

import numpy as np
import cv2
import display_functions as df
import dct_function as dct
import video_function as vf
import entropy as en

img1 = cv2.imread("MikeySpiece_square.png",0)
img2 = cv2.imread("MikeySpiece.png",0)

# Part 1: Intra-Frame Coding(DCT)

img = img1

# M x M Image

# convert to floating point and scaling
imf = np.float32(img)

# computing dct
imf_dct = cv2.dct(imf)

# convert to int
img_dct = np.int(imf_dct)

df.display_multiple_images([img, img_dct])

# 4 x 4 Image

# Crop image
img_4 = img[142:146,113:117]

imf_4 = np.float32(img_4)

# Compute DCT
imf_4_dct = cv2.dct(imf_4)

# Converting back to image array
imf_4_idct = cv2.idct(imf_4_dct)
img_4_idct = np.uint8(imf_4_idct)

# Display Image
# imf_4_logdct = np.log(abs(imf_4_dct))

# img_4_dct = np.uint8(imf_4_dct * 255)


# 8 x 8 Image

# Crop image
img_8 = img[142:150,113:121]

imf_8 = np.float32(img_8)/255

imf_8_dct = cv2.dct(imf_8)

# Converting back to image array
imf_8_idct = cv2.idct(imf_8_dct)
img_8_idct = np.uint8(imf_8_idct * 255)


# img_8_dct = np.uint8(imf_8_dct * 255)

# 32 x 32 Image

# Crop image
img_32 = img[142:174,113:145]

imf_32 = np.float32(img_32)/255

imf_32_dct = cv2.dct(imf_32)

# img_32_dct = np.uint8(imf_32_dct * 255)

# Converting back to image array
imf_32_idct = cv2.idct(imf_32_dct)
img_32_idct = np.uint8(imf_32_idct * 255)


# Andrew i'll leave part 4 to you
# Just remove values from imf_8_dct to achieve this

# Creating copy of dct to test
imf_test = imf_8_dct.copy()

# 8 x 8 Block DCT and IDCT
img = img2.copy()

imf = np.float32(img)

imf_dct = dct.dct_split(imf)

imf_quant = dct.quantization(imf_dct, 4)

img_quant = dct.idct_split(imf_quant)

df.display_multiple_images([img, img_quant])


# MSE

# SNR

# PSNR

# Part 2 - Inter-Frame Coding

video = cv2.VideoCapture("stephen.gif")
rate = video.get(5)

# Question 1

# Extract 2 frames
f = 2
vid = vf.frame_extract(video, f)

vf.display_video(vid, int(rate / 5))

# Difference Frame of both frames
frame_diff = vid[1] - vid[0]

# Display Difference Frame
df.display_image(frame_diff)

# Question 2

# Extract Frames
f = 11
vid = vf.frame_extract(video, f)
video.release()

frame_diff = []
entropy = []

for i in range(0, f-1):
    frame_diff.append(vid[i + 1] - vid [i])
    stats, ent = en.myEntropy(frame_diff[i])
    entropy.append(ent)
    
# Question 3

# Question 4

