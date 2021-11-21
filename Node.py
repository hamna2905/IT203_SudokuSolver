# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 12:19:52 2021

@author: shala
"""

class Node:
    def __init__(self, idx, data) : # Constructor   
        """
        id : Integer (1, 2, 3, ...)
        """
        self.id = idx
        self.data = data
        self.connectedTo = dict()


  #  def createEdge(n,node):
      #  for i in range(n**2):
          
    def printNode(self):
        print(self.data)
        
           
       
         