# Start of import
import networkx as nx
# End of import

# Start of GreedyBestFirst(graph, list of Node objects)
def GreedyBestFirst(G, nodes):
    path = []
    buffer = []
    neighbors = []

    path.append(list(G.nodes)[0])

    while (True):

        if (nodes[path[-1]].getHeuristic() == 0):
            return path

        for ele in list(nx.neighbors(G, path[-1])):
            if (ele not in path):
                neighbors.append(ele)

        # bufferFiller(list of possible nodes, list to be filled with neighbors to our current position, list of our current path, list of Node objects)
        bufferFiller(buffer, neighbors, path, nodes)

        if (buffer == []):
            print("Node not found")
            break

        # Choosing the node with the minimum heuristic from the buffer
        # nextNode is a list under this structure: nextNode = [chosen node's name, its predecessor's name, its heuristic]
        nextNode = getMin(buffer)

        # Checking if the last node in the path is the predecessor of the chosen node or we will have to go back to its predecessor
        if (nextNode[1] == path[-1]):
            path.append(nextNode[0])
        else:
            clearPath(path, nextNode[1])
            path.append(nextNode[0])
# End of GreedyBestFirst

# Start of bufferFiller(list of possible nodes, list to be filled with neighbors to our current position, list of our current path, list of Node objects)
# This function will fill the buffer with the neighbors of the last node in the path under the form: [neighbor's name, predecessor's name, neighbor's heuristic]
def bufferFiller(buffer, neighbors, path, nodes):
    for ele in neighbors:
        if ([ele, path[-1], nodes[ele].getHeuristic()] not in buffer):
            buffer.append([ele, path[-1], nodes[ele].getHeuristic()])
    neighbors.clear()
# End of bufferFiller

# Start of getMin(list of possible nodes)
# This function will return the index of the neighbor  with the minimal heuristic in buffer
def getMin(buffer):
    min = 0
    for i in range(len(buffer)-1):
        if (buffer[i][2] > buffer[i+1][2]):
            min = i+1
    return buffer.pop(min)
# End of getMin

# Start of clearPath(list of our current path, the name of the predecessor of the chosen node)
# This function will clear the path in case we find a better one
def clearPath(path, origin):
    for i in range(len(path)):
        if (path[i] == origin):
            break

    for j in range(i+1, len(path)):
        path.pop(j)
# End of clearPath