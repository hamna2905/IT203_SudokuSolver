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
                    
    
                    