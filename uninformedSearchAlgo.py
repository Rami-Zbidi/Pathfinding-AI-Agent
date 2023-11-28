# Start of import
import networkx as nx
# End of import

# Start of BreadthFirst(graph, the destination name)
def BreadthFirst (G, node):
    queue = []
    visited = []

    queue.append(list(G.nodes)[0])

    while (queue != []):
        visited.append(queue[0])

        if (queue[0] == node):
            return visited

        # Adding to the queue the neighbors of the first node in the queue that have not been visited nor are already in the queue
        for ele in list(nx.neighbors(G, queue[0])):
            if (ele not in queue) and (ele not in visited):
                queue.append(ele)

        # Dequeuing the queue
        queue.pop(0)

    return "Node not found"
# End of BreadthFirst

# Start of DepthFirst(graph, the destination name)
def DepthFirst (G, node):
    stack = []
    visited = []

    stack.append(list(G.nodes)[0])

    while (stack != []):

        if (stack[-1] not in visited):
            visited.append(stack[-1])

        if (stack[-1] == node):
            return visited

        # Popping the top node of the stack if it's a leaf node
        if (set(nx.neighbors(G, stack[-1])).issubset(set(stack))) or (set(nx.neighbors(G, stack[-1])).issubset(set(visited))):
            stack.pop(len(stack)-1)

        # Adding the neighbors of the top node of the stack going from left to right
        if (stack != []):
            for ele in list(nx.neighbors(G, stack[-1])):
                if (ele not in visited):
                    stack.append(ele)
                    break

    return "Node not found"
# End of DepthFirst