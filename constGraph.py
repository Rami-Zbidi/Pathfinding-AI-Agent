# Start of importing
import networkx as nx
import math
# End of importing

# Start of defining the class Node that takes the node's name and heuristic as attributes
class Node:
    def __init__ (self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

    def getName(self):
        return self.name

    def getHeuristic(self):
        return self.heuristic
# End of defining the class Node

# Start of calHeuristic(current position's coordinations, destination's coordinations)
def calHeuristic(currentCoords, destCoords):
    return math.sqrt(pow(currentCoords[0] - destCoords[0], 2) + pow(currentCoords[1] - destCoords[1], 2))
# End of calHeuristic

# Start of constructGraph(graph, list of lists [,destination's coordinations])
def constructGraph(G, plot, destCoords = None):
    neighbors = []
    nodes = {}

    for i in range(1,len(plot)+1):
        for j in range(len(plot[0])):
            # We will only handle non empty tiles
            if (plot[i-1][j] != ""):
                if (i-1 != 0) and (plot[i-2][j] != ""):
                    neighbors.append(plot[i-2][j]+str(i-1))

                if (j != 0) and (plot[i-1][j-1] != ""):
                    neighbors.append(plot[i-1][j-1]+str(i))

                if (i-1 != 8) and (plot[i][j] != ""):
                    neighbors.append(plot[i][j]+str(i+1))

                if (j != 8) and (plot[i-1][j+1] != ""):
                    neighbors.append(plot[i-1][j+1]+str(i))

                # We will create a Node object and calculate the heuristic only if the destination's coordinations were given as parameter
                if (destCoords != None):
                    currentNode = Node(plot[i-1][j]+str(i), calHeuristic([i-1, j],destCoords))
                    nodes[plot[i-1][j]+str(i)] = currentNode

                G.add_node(plot[i-1][j]+str(i))

                for node in neighbors:
                    if (G.has_edge(plot[i-1][j]+str(i), node) == False):
                        G.add_edge(plot[i-1][j]+str(i), node);

                neighbors = []
    return nodes
# End of constructGraph