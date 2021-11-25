
class Node:
    def __init__(self, idx, data) : # Constructor   
        
        self.id = idx
        self.data = data
        self.connectedTo = dict()
        

  
          
    def printNode(self):
        print(self.data)
        
#function to access and change data using id-done
    def setData(self,data):
        self.data=data

    def getData(self,data):
        return self.data

    
    def updateDict(self,key,rows,col,block):
        value=list()
        value.append(rows)
        value.append(col)
        value.append(block)
        d={key: value}
        self.connectedTo.update(d)

   
            