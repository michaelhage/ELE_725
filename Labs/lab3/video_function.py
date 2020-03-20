# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 01:30:07 2020

@author: Michael Hage
"""

import cv2
import numpy as np

def frame_extract(video, f):
    
    img = []
    frames_counter = 0
    
    while frames_counter < f:
        frames_counter += 1
        check, frame = video.read()
        # print(frame)
        # print(check)
        if check:
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            img.append(gray)
            
            # cv2.imshow("Capturing", gray)
            # key = cv2.waitKey(1)
        else:
            break
    
    return np.uint8(img)

def display_video(video, rate):
    
    for i in range(0, len(video)):
        cv2.imshow("Frame: " + str(i+1),video[i])
        # key = cv2.waitKey(rate)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def DCPM_encoder(vid, sel):
    
    if(sel == 1):
        
    elif(sel == 2):
    
    elif(sel == 3):
    
    elif(sel == 4):
    
    else:
        print("Incorrect Selection Value. Please Select Integer Value in range 1-4")
        return 0