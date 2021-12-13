from Node import Node
from Graph import Graph


class GraphColoring:

    def __init__(self):
        pass
        
    def StepOne(self,graph):
        flag = True
        idtrack=list()
        while flag== True:
            flag = False
            for node in graph.node_array:
                
                arr=graph.possibleValues(node.id)

                if(node.data==0 and len(arr)==1):
                    flag = True
                    graph.updateData(node.id,arr[0])
                    idtrack.append(node.id)
                    

                # if(node.data==0 and len(arr)==0):
                #     flag=False
                #     length=len(idtrack)
                #     for j in range (length):
                #         # print(node.id)
                #         graph.updateData(idtrack[j],0)
                    
                #     idtrack.clear()
                #     if flag==False and len(arr)==0:
                #         return 0

                #     if flag==False:
                #         break    
            
                    # if len(arr)==0:
                    #     return 0
        # return 1                    
                



    
                    
    def generateList(graph):
            values = list()
            for i in range(8):
                vals = list()
                values.append(vals)
            for node in graph.node_array:
                if(node.data==0):
                    values[len(graph.possibleValues(node.id))-2].append(node.id)
            for i in range(1,8):
                values[0] = values[0]+values[i]
            return values[0]


    def StepTwo(self, graph, num, values):
        #print(values[num])
        if num==len(values):
            return 1
        node_id = values[num]
        arr = graph.possibleValues(node_id)
        if len(arr)==9:
            print("9") 
        
        for i in arr:
            graph.updateData(node_id,i)
            if self.StepTwo(graph, num+1, values)==1:
                return 1
        graph.updateData(node_id,0)
        return 0

                        
    # def printConnected(self,graph):
    #         for node in graph.node_array:
    #             print(node.connectedTo )





board = [
            [5,0,9,4,0,0,0,0,0],
            [0,0,3,0,0,0,6,9,0],
            [0,1,0,0,0,0,0,0,5],
            [0,5,0,1,8,0,0,0,0],
            [3,0,0,0,5,0,0,0,7],                #hard
            [0,0,0,0,9,6,0,5,0],
            [9,0,0,0,0,0,0,7,0],
            [0,3,8,0,0,0,5,0,0],
            [0,0,0,0,0,7,1,0,3]
    ]
        
    # board = [
    #     [1,0,0,4,8,9,0,0,6]
    #    ,[7,3,0,0,5,0,0,4,0]
    #    ,[4,6,0,0,0,1,2,9,5]
    #    ,[3,8,7,1,2,0,6,0,0]
    #    ,[5,0,1,7,0,3,0,0,8]
    #    ,[0,4,6,0,9,5,7,1,0]
    #    ,[9,1,4,6,0,0,0,8,0]                   
    #    ,[0,2,0,0,4,0,0,3,7]
    #    ,[8,0,3,5,1,2,0,0,4]

    #     ]
        
G=  Graph(9,board)
C = GraphColoring()
G.createEdge(9)
G.displayGraph(9)
print("\n")
C.StepOne(G)  

   
values = GraphColoring.generateList(G)
if len(values)!=0:
    C.StepTwo(G, 0, values)
print('\n SOLUTION\n')
G.displayGraph(9)


# print("\n \n After Step 2 Solving \n")



            # [0,0,0,4,0,0,0,0,0],
            # [4,0,9,0,0,6,8,7,0],
            # [0,0,0,9,0,0,1,0,0],
            # [5,0,4,0,2,0,0,0,9],                      
            # [0,7,0,8,0,4,0,6,0],
            # [6,0,0,0,3,0,5,0,2],
            # [0,0,1,0,0,7,0,0,0],
            # [0,4,3,2,0,0,6,0,5],
            # [0,0,0,0,0,5,0,0,0]
            # 
            # 
            #     
            # [0,9,1,0,7,0,0,0,0],
            # [2,0,3,0,0,0,0,5,0],
            # [0,0,0,4,0,2,9,0,7],
            # [0,0,2,8,0,6,0,0,9],
            # [0,0,0,0,0,0,0,0,0],            
            # [9,0,0,1,0,4,6,0,0],
            # [1,0,5,2,0,7,0,0,0],
            # [0,8,0,0,0,0,5,0,1],
            # [0,0,0,0,1,0,7,6,0]               



#             [5,0,9,4,0,0,0,0,0]
            # [0,0,3,0,0,0,6,9,0],
            # [0,1,0,0,0,0,0,0,5],
            # [0,5,0,1,8,0,0,0,0],
            # [3,0,0,0,5,0,0,0,7],
            # [0,0,0,0,9,6,0,5,0],
            # [9,0,0,0,0,0,0,7,0],
            # [0,3,8,0,0,0,5,0,0],
            # [0,0,0,0,0,7,1,0,3]