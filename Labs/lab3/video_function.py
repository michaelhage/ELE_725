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
    
def DCPM_encoder(vid, pre, sel):
    
    vid_dpcm = vid.copy()
    
    if(sel == 1):
        
        for i in range(1, len(vid)): 
            temp = pre[i-1]
            vid_dpcm[i,:,1:] = temp[:,0:len(vid[i,0])-1]
    elif(sel == 2):
        
        for i in range(1, len(vid)): 
            temp = pre[i-1]
            vid_dpcm[i,1:,:] = temp[0:len(vid[i])-1,:]
            
    elif(sel == 3):
        
        for i in range(1, len(vid)): 
            temp = pre[i-1]
            vid_dpcm[i,1:,1:] = temp[0:len(vid[i])-1,0:len(vid[i,0])-1]
            
    elif(sel == 4):
        for i in range(1, len(vid)): 
            temp = pre[i-1]
            for x in range(1, len(temp)):
                for y in range(1, len(temp)-1):
                        # A + B - C
                        vid_dpcm[i,x,y] = temp[x-1,y] + temp[x, y-1] - temp[x-1,y-1]
    else:
        print("Incorrect Selection Value. Please Select Integer Value in range 1-4")
        return 0
    
    return vid_dpcm