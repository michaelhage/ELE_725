# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 23:09:00 2020

@author: Michael Hage
"""

class Huffman(object):
    # Define a Node
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        
    # Get Left Node
    def get_left(self):
        return self.left
    # Get Right Node
    def get_right(self):
        return self.right
    
        
def create_huffman(dictionary):
    
    dict_list = list()
    
    # Converts the dictionary to a ordered list
    for key, value in dictionary.items():
        temp = [key, value]
        dict_list.append(temp)
    
    # Sorts list by frequency
    dict_list.sort(key=lambda tup: tup[1])
    
    while(len(dict_list) != 1):
        
        # Create Node Links
        node = Huffman(dict_list[0][0], dict_list[1][0])
        
        # Gets node frequency
        temp = [node,dict_list[0][1] + dict_list[1][1]]
        
        # Deletes the two values used above
        dict_list.pop(0)
        dict_list.pop(0)
        
        # Append new node to list and sort its position
        dict_list.append(temp)
        dict_list.sort(key=lambda tup: tup[1])