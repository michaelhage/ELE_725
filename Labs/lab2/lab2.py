# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:45:49 2020

@author: Michael
"""
import cv2
import numpy as np
import entropy as en
import display_functions as df
import huffman

# String
str1 = "HUFFMAN IS THE BEST COMPRESSION ALGORITHM"
str_dict, str_ent = en.myEntropy(str1)

print("Entropy of String: "+ str(str_ent))
print("Compression Ratio: " + str(8.0/str_ent))

# Grayscale Image
img2 = cv2.imread("bridge.jpg", 0)
df.display_image(img2)

img2_dict, img2_ent = en.myEntropy(img2)

df.histogram(img2_dict)

print("Entropy Channel: "+ str(img2_ent))
print("Compression Ratio: " + str(8.0/img2_ent))

# Colored Image
img1 = cv2.imread("MikeySpiece.png", 1)
df.display_image(img1, 'Self Portrait')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)

img1_dict_Cr, img1_ent_Cr = en.myEntropy(img1[1])
img1_dict_Cb, img1_ent_Cb = en.myEntropy(img1[2])

print("Entropy Cr Channel: "+ str(img1_ent_Cr))
print("Compression Ratio for Cr Channel: " + str(8.0/img1_ent_Cr))

print("Entropy Cr Channel: "+ str(img1_ent_Cb))
print("Compression Ratio for Cr Channel: " + str(8.0/img1_ent_Cb))

df.histogram(img1_dict_Cr)
df.histogram(img1_dict_Cb)

# Huffman Encoding

# Sample String
str1 = "HUFFMAN IS THE BEST COMPRESSION ALGORITHM"

dict_str, en_str = en.myEntropy(str1)

node, tree = huffman.create_huffman(dict_str)

encode = huffman.encode_huffman_string(tree, str1)

decode = huffman.decode_huffman_string(node, encode)

print("Original: " + str1)
print("Encoded: " + encode)
print("Decoded: " + decode)

print("Compression Ratio: " + str( len(str1) * 8 / len(encode)))

# Grayscale Image
img = img2

img_dict, img_ent = en.myEntropy(img)

node, tree = huffman.create_huffman(img_dict)

encode = huffman.encode_huffman_array(tree, img2)

decode = huffman.decode_huffman_array(node, encode)
decode = np.array(decode, np.uint8)

df.display_image(img, title='Original')
df.display_image(decode, title='Decoded')

compress = 0
for i in range(0,len(encode)):
    compress += len(encode[i])

print("Compression Ratio: " + str(np.size(img) * 8 / compress))