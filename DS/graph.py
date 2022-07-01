#graphs can be implemented using adjacent matrix, adjancy list, edge list. Below implementation is using adjacent list

def addVertex(value):
    global graph
    if value in graph:
        print("value {} exists in graph".format(value))
    else:
        graph[value] = []

def addEdge(start,end,weight):
    global graph
    if start not in graph:
        print("{} not in graph".format(start))
    else:
        temp = [end,weight]
        graph[start] = temp

def printGraph():
    global graph
    for ele in graph:
        print(str(ele) + "->" + str(graph[ele][0]))

if __name__ == "__main__":
    graph = {}
    addVertex(10)
    addVertex(20)
    addVertex(30)
    addVertex(40)
    addEdge(10,20,2)
    addEdge(20,30,3)
    addEdge(30,40,1)
    addEdge(40,10,5)
    printGraph()