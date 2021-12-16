import copy
from Node import Node
import numpy as np
class Graph:
    
    def __init__(self,n,matrix):
        self.node_array = list()
        self.order=n
       
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

        self.grid=np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                self.grid[i][j]=pos
                pos+=1

        for i in range(n):
           for j in range(n):
              node=Node(count,matrix[i][j])
              self.node_array.append(node)
              count+=1
              
    def displayGraph(self,n):
        for i in range (0,len(self.node_array)):
            if i%n==0:
                print("\n")
                print(self.node_array[i].printNode(),end="   ")
            else:
                print(self.node_array[i].printNode(),end="   ")

    def updateData(self,id,data):
        for i in range(len(self.node_array)):
            if self.node_array[i].id==id:
                self.node_array[i].setData(data)
                
                break
            
    def createEdge(self,order):         #put in graph class
        for i in range(0,order):
            for j in range(0,order):
                key=self.grid[i][j]
                rows=list()
                for k in range(0,order):
                    value=self.grid[i][k]
                    if value!=key:
                     rows.append(value)

                cols =list()
                for k in range(0,order):
                    value=self.grid[k][j]
                    if value!=key:
                        cols.append(value)


                block=list()
                if key in self.block1:
                    block=copy.deepcopy(self.block1)
                elif key in self.block2:
                    block=copy.deepcopy(self.block2)
                elif key in self.block3:
                    block=copy.deepcopy(self.block3)
                elif key in self.block4:
                    block=copy.deepcopy(self.block4)
                elif key in self.block5:
                    block=copy.deepcopy(self.block5)
                elif key in self.block6:
                    block=copy.deepcopy(self.block6)
                elif key in self.block7:
                    block=copy.deepcopy(self.block7)
                elif key in self.block8:
                    block=copy.deepcopy(self.block8)
                elif key in self.block9:
                    block=copy.deepcopy(self.block9)

                block.remove(int(key))

                index=int(key-1)
                self.node_array[index].updateList(index,rows,cols,block) 
                
                
    def possibleValues(self, key):
        possible_values = list()
        for i in range(self.order):
            possible_values.append(i+1)
            
        arr=self.node_array[int(key-1)].connectedTo
        
        for i in arr:

            if self.node_array[int(i-1)].data in possible_values:
        
                
                possible_values.remove(self.node_array[int(i-1)].data)
                
                # print(key)
                # print(possible_values)
        
        return possible_values
                    
                
                
    





