
from Node import Node
import numpy as np
class Graph:
    
    def __init__(self,n,matrix):
        self.node_array = list()
       
        count=1
        pos=1
        
        self.block1=[1,2,3,10,11,12,19,20,21]
        self.block2=[4,5,6,13,14,15,22,23,24]
        self.block3=[7,8,9,16,17,18,25,26,27]
        self.block4=[28,29,30,37,38,39,46,47,48]
        self.block5=[31,32,33,40,41,42,49,50,51]
        self.block6=[34,35,36,43,44,45,52,53,54]
        self.block7=[55,56,57,64,65,66,73,74,75]
        self.block8=[58,59,60,67,68,69,76,77,78]
        self.block9=[61,62,63,70,71,72,79,80,81]

        grid=np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                grid[i][j]=pos
                pos+=1

        for i in range(n):
           for j in range(n):
              n=Node(count,matrix[i][j])
              self.node_array.append(n)
              count=+1
              
    def displayGraph(self,n):
        for i in range (0,len(self.node_array)):
            if i%n==0:
                print("\n")
            else:
                print(self.node_array[i].printNode())

    def updateData(self,id,data):
        for i in range(len(self.node_array)):
            if self.node_array[i].id==id:
                self.node_array[i].setData(data)
    
    def createEdge(self,order,grid):         #put in graph class
        for i in range(order):
            for j in range(order):
                key=grid[i][j]
                rows=list()
                for k in range(0,order):
                    value=grid[i][k]
                    if value!=key:
                     rows.append(value)

                cols =list()
                for k in range(0,order):
                    value=grid[k][j]
                    if value!=key:
                        cols.append(value)


                        block=list()
                if key in self.block1:
                    block=self.block1
                elif key in self.block2:
                    block=self.block2
                elif key in self.block3:
                    block=self.block3
                elif key in self.block4:
                    block=self.block4
                elif key in self.block5:
                    block=self.block5
                elif key in self.block6:
                    block=self.block6
                elif key in self.block7:
                    block=self.block7
                elif key in self.block8:
                    block=self.block8
                elif key in self.block9:
                    block=self.block9

                
                self.node_array[key].updateList(key,rows,cols,block) 
                
                
    def possibleValues(self, key):
        possible_values = [1,2,3,4,5,6,7,8,9]
        for i in self.node_array[key-1].connectedTo:
            if self.node_array[i-1].data in possible_values:
                possible_values.remove(self.node_array[i-1].data)
        
        return possible_values
                    
                
                
    



            
   
                            
     
            
         
            