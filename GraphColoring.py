from Node import Node
from Graph import Graph

class GraphColoring:
    
    def StepOne(graph):
        flag = True
        while flag is True:
            flag = False
            for node in graph.node_array:
                if(node.data!=0 and graph.possibleValues(node.id).len()==1):
                    flag = True
                    node.setData(graph.possibleValues(node.id)[0])
                    
    
     

    board = [
        [0,0,0,4,0,0,0,0,0],
        [4,0,9,0,0,6,8,7,0],
        [0,0,0,9,0,0,1,0,0],
        [5,0,4,0,2,0,0,0,9],
        [0,7,0,8,0,4,0,6,0],
        [6,0,0,0,3,0,5,0,2],
        [0,0,1,0,0,7,0,0,0],
        [0,4,3,2,0,0,6,0,5],
        [0,0,0,0,0,5,0,0,0]
        ]
        

 
    G=  Graph(9,board)
    
    G.displayGraph(9)

            # [0,0,0,4,0,0,0,0,0],
            # [4,0,9,0,0,6,8,7,0],
            # [0,0,0,9,0,0,1,0,0],
            # [5,0,4,0,2,0,0,0,9],
            # [0,7,0,8,0,4,0,6,0],
            # [6,0,0,0,3,0,5,0,2],
            # [0,0,1,0,0,7,0,0,0],
            # [0,4,3,2,0,0,6,0,5],
            # [0,0,0,0,0,5,0,0,0]                   