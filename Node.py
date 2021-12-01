
class Node:
    def __init__(self, idx, data) : # Constructor   
        
        self.id = idx
        self.data = data
        self.connectedTo = list()
        

  
          
    def printNode(self):
        return (self.data)
        
#function to access and change data using id-done
    def setData(self,data):
        self.data=data

    def getData(self,data):
        return self.data

    
    def updateList(self,key,rows,col,block):
        value=list()
        value.append(rows)
        value.append(col)
        value.append(block)
        self.connectedTo[key]=value
        
        
        
        
        

   
            