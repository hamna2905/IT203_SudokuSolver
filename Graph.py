# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 12:21:46 2021

@author: shala
"""
import Node
import numpy as np
class Graph:
    
    def __init__(self,n,matrix):
        node_array = list()
       
        count=1
        pos=1
        
        grid=np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                grid[i][j]=pos;
                pos+=1

        for i in range(n):
           for j in range(n):
              n=Node(count,matrix[i][j])
              node_array.append(n)
              count=+1
              
    def displayGraph(n,node_array):
        for i in node_array:
            if i%n==0:
                 print("\n")
            else:
                print(node_array[i].printNode())
            
    def createEdge(grid):
                            
         
            
         
            