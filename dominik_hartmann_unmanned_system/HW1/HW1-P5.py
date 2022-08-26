# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:53:32 2022

@author: dhart
"""
import numpy as np


def node_distance(x_1, y_1, x_2, y_2):
    distance = np.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2);
    return distance

print(node_distance(2, 1, 3, 2))