from map import *
from node_queue import *


def breadth_first_search_1(graph, start):
    # print out what we find
    unexplored = Queue()
    unexplored.put(start)
    explored = {}
    explored[start] = True

    # While there are still unexplored nodes
    while not unexplored.empty():
        # Get the next unexplored node
        current = unexplored.get()
        print("Visiting %r" % current)
        for next_node in graph.neighbors(current):
            # If the neighbour is unexplored, explore it
            if next_node not in explored:
                unexplored.put(next_node)
                explored[next_node] = True


def breadth_first_search_2(graph, start, end):
    # return "explored"
    unexplored = Queue()
    unexplored.put(start)
    explored = {}
    explored[start] = None

    while not unexplored.empty():
        current = unexplored.get()
        if current == end:
            return explored
        for next_node in graph.neighbors(current):
            if next_node not in explored:
                unexplored.put(next_node)
                explored[next_node] = current
        g.draw_grid(current, explored, start, end)
        sys.stdout.write("\n")

    return explored


# # Create a sample graph
# example_graph = SimpleGraph()
# example_graph.edges = {
#     'A': ['B'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A'],
#     'D': ['E', 'A'],
#     'E': ['B', 'F'],
#     'F': []
# }
#
# breadth_first_search_1(example_graph, 'C')

g = SquareGrid(30, 15)
#g.walls = DIAGRAM1_WALLS

parents = breadth_first_search_2(g, (8, 7), (25, 11))
# Visited, Start, End
g.draw_grid((-1, -1), parents, (8, 7), (25, 11))
