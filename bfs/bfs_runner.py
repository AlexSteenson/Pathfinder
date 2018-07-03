from map import *
from node_queue import *


def breadth_first_search(graph, start, end):
    # return "explored"
    unexplored = Queue()
    unexplored.put(start)
    explored = {}
    explored[start] = None

    while not unexplored.empty():
        current = unexplored.get()
        if current == end:
            break

        for next_node in graph.neighbors(current):
            if next_node not in explored:
                unexplored.put(next_node)
                explored[next_node] = current

        g.draw_grid(current, explored, start, end)
        sys.stdout.write("\n")

    return explored


g = SquareGrid(30, 15)
g.walls = [(9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 14), (9, 13), (9, 3)]
begin = (8, 7)
goal = (25, 11)
parents = breadth_first_search(g, begin, goal)
path = g.reconstruct_path(parents, begin, goal)
# Visited, Start, End
g.draw_grid((-1, -1), path, (8, 7), (25, 11))
