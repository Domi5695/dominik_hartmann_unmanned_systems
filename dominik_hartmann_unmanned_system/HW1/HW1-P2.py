# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:50:26 2022

@author: dhart
"""

if __name__== '__main__':
    class node(object):
        def __init__(self, x, y, parent_cost, index):
            self.x = x
            self.y = y
            self.pc = parent_cost
            self.i = index
            
            