# Start of import
import networkx as nx
import matplotlib.pyplot as plt
from constGraph import *
from informedSearchAlgo import *
from uninformedSearchAlgo import *
# End of import

if __name__ == '__main__':
    G = nx.Graph()

    # Representing the board tiles with a list of lists
    # Each letter corresponds to the columns letter and the list index will represent the numbers
    field = [
        ["A", "", "C", "", "E", "F", "G", "", "I"],
        ["A", "B", "C", "D", "", "F", "", "H", ""],
        ["", "B", "C", "D", "E", "", "G", "H", "I"],
        ["A", "B", "", "D", "E", "F", "G", "", "I"],
        ["A", "B", "C", "", "", "F", "G", "H", "I"],
        ["", "B", "C", "", "E", "", "", "H", ""],
        ["A", "", "C", "D", "E", "", "G", "H", ""],
        ["", "", "C", "D", "", "F", "", "H", "I"],
        ["A", "", "", "D", "", "F", "G", "H", "I"]
    ]

    # Constructing the node using constructGraph(graph, list of lists, destination coordinations)
    # constructGraph returns a list of Node objects of the nodes that have been added to the graph
    nodes = constructGraph(G, field, [8, 8])

    # Finding the path to the destination using BreadthFirst(graph, destination name)
    print("The sequence of nodes explored to reach the I9 using breadth first:", BreadthFirst(G, "I9"),"\n")

    # Finding the path to the destination using DepthFirst(graph, destination name)
    print("The sequence of nodes explored to reach the I9 using depth first:", DepthFirst(G, "I9"),"\n")

    # Finding the path to the destination using GreedyBestFirst(graph, list of Node objects, destination name)
    print("The path using Greedy Best First algorithm: ",GreedyBestFirst(G, nodes))

    # displaying the graph G
    nx.draw(G, with_labels=True)
    plt.show()