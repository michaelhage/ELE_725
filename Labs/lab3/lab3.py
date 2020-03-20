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

cv2.imwrite("img4.png", img_4)

imf_4 = np.float32(img_4)

# Compute DCT
imf_4_dct = cv2.dct(imf_4)

# Converting back to image array
imf_4_idct = cv2.idct(imf_4_dct)
img_4_idct = np.uint8(imf_4_idct)

# Display Image
df.display_multiple_images([img_4, img_4_idct])

# Scaling image and then displaying colormap
img_4_scale = np.log( abs(imf_4_dct) )
df.colormap(img_4_scale)

# 8 x 8 Image

# Crop image
img_8 = img[142:150,113:121]

cv2.imwrite("img8.png", img_8)

imf_8 = np.float32(img_8)/255

imf_8_dct = cv2.dct(imf_8)

# Converting back to image array
imf_8_idct = cv2.idct(imf_8_dct)
img_8_idct = np.uint8(imf_8_idct * 255)

df.display_multiple_images([img_8, img_8_idct])

# Scaling image and then displaying colormap
img_8_scale = np.log( abs(imf_8_dct) )
df.colormap(img_8_scale)

# 32 x 32 Image

# Crop image
img_32 = img[142:174,113:145]

cv2.imwrite("img32.png", img_32)

imf_32 = np.float32(img_32)/255

imf_32_dct = cv2.dct(imf_32)

# Converting back to image array
imf_32_idct = cv2.idct(imf_32_dct)
img_32_idct = np.uint8(imf_32_idct * 255)

df.display_multiple_images([img_32, img_32_idct])

# Scaling image and plotting colormap
img_32_scale = np.log( abs(imf_32_dct) )
df.colormap(img_32_scale)

# Question 4

img = img1[100:200,100:200]
cv2.imwrite("img_test.png", img)
df.display_image(img)

imf = np.float32(img)
imf_dct = cv2.dct(imf)

# DC Component

# Creating copy of dct to test
imf_test = imf_dct.copy()

# DC Component removal
imf_test[0,0] = 0

img_test = np.uint8(cv2.idct(imf_test) * 255)
df.display_image(img_test)

cv2.imwrite("img_DC.png", img_test)

# Low Frequency
imf_test = imf_dct.copy()

imf_test[1:int(len(imf_test)/4),1: int(len(imf_test[0])/4)] = 0
img_test = np.uint8(cv2.idct(imf_test) * 255)
df.display_image(img_test)

cv2.imwrite("img_LF.png", img_test)

# High Frequency
imf_test = imf_dct.copy()

imf_test[int(len(imf_test)/4): , int(len(imf_test[0])/4) :] = 0
img_test = np.uint8(cv2.idct(imf_test) * 255)
df.display_image(img_test)

cv2.imwrite("img_HF.png", img_test)

# Question 5&6

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

# Taking the amoount of bits needed to encode an individual pixel across an 
# entire video and then dividing it by the sum of the entropy that will encode
# the pixel
compression_ratio = 8 * len(vid) / (8 + sum(entropy))

print("The presumed compression ratio for the video is" + str(compression_ratio))

# Question 4

# Selector, choose an integer in the range 1-4
sel = 2

vid_dpcm = vf.DCPM_encoder(vid, frame_diff, sel)

# Question 5
n = 3
# Adjacent Frames
df.display_multiple_images([vid[n], vid[n+1], vid[n+2]])

# Frame Difference
df.display_multiple_images([frame_diff[n], frame_diff[n+1]])

# Histograms

# First Frame
stats = df.hashmap(vid[n])
df.histogram(stats)

# Second Frame
stats = df.hashmap(vid[n+1])
df.histogram(stats)

# Third Frame
stats = df.hashmap(vid[n+2])
df.histogram(stats)

# DPCM Coded 1
stats = df.hashmap(frame_diff[n])
df.histogram(stats)

stats = df.hashmap(frame_diff[n+1])
df.histogram(stats)