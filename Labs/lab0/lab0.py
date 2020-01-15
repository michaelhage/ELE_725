# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:56:37 2020

@author: Michael Hage
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from scipy.fftpack import fft, ifft
import simpleaudio as sa

import basic_functions as bf

# Load Audio

Fs, aud = read("ELE725_audio.wav")
aud = np.int16(aud)

play_obj = sa.play_buffer(aud, 2, 2, Fs)
play_obj.wait_done()

play_obj = sa.play_buffer(aud, 2, 2, np.int(Fs/2)) 
play_obj.wait_done()

#  Load Image

img1 = cv2.imread("lena.jpg", 1)
img2 = cv2.imread("lena.jpg", 0)

bf.display_multiple_images([img1, img2])

# Load Video

video = cv2.VideoCapture("keypad.avi")   
frames_counter = 1

while True:
    frames_counter += 1
    check, frame = video.read()
    # print(frame)
    # print(check)
    if check:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capturing", gray)
        key = cv2.waitKey(1)
    else:
        break

print("Number of frames in the video: ", frames_counter)
video.release()
cv2.destroyAllWindows()

# Load Webcam

mirror = False

cam = cv2.VideoCapture(0)
while True:
    ret_val, img = cam.read()
    if mirror: 
        img = cv2.flip(img, 1)
    cv2.imshow('my webcam', img)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
cv2.destroyAllWindows()