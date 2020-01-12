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

Fs, aud = read("ELE725_audio.wav")
aud = np.int16(aud)

play_obj = sa.play_buffer(aud, 2, 2, Fs)

play_obj.wait_done()