# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:10:40 2022

@author: dhart
"""
import matplotlib.pyplot as plt
import numpy as np

    
if __name__== '__main__':
    #functions:
    def rowlen(minX, maxX, space):
        return (maxX-minX)/space + 1;
    
    def columnlen(minY, maxY, space):
        return (maxY-minY)/space + 1;
    
    def node_index(x, y, maxX, maxY, minX, minY, space):
        return x/space + y*(rowlen(minX, maxX, space)/space)
    
    # Inputs:
    maxX=10;
    maxY=10;
    minX=0;
    minY=0;
    space=0.5; #grid Spacing
    
    x = 5; #test
    y = 1.5; #test
    
    X = np.arange(minX, maxX + space, space)
    Y = np.arange(minY, maxY + space, space)
    
    index = np.array([]);
    #calculate all the index we need:
    index = np.arange(0, rowlen(minX, maxX, space)*columnlen(minY, maxY, space))
    #for n in range (0, 439):
        #index = np.append(index, node_index(X[0], Y[0], maxX, maxY, minX, minY, space))
    
    
    # plot:
    fig, ax = plt.subplots()
    ax. set(xlim=(minX, maxX + 0.5),
            ylim=(minY, maxY + 0.5))
    #Plot every index-number for each node
    
    for i in range(0, int(rowlen(minX, maxX, space))):
        for j in range(0, int(columnlen(minY, maxY, space))):
            plt.text(X[i], Y[j], str(int(index[i + j*int(rowlen(minX, maxX, space))])), color="red", fontsize=8);
            if i == x/space:
                if j == y/space:
                    print(index[i + j*int(rowlen(minX, maxX, space))])
        
    ax.scatter(x, y, color="blue")
    
    plt.show()
                    