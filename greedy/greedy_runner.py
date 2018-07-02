from map import *
import Queue as Q


def calculate_manhattan_distance(start, end):
    (start_x, start_y) = start
    (end_x, end_y) = end
    return abs(start_x - end_x) + abs(start_y - end_y)


def greedy_search(graph, start, end):
    # return "explored"
    unexplored = Q.PriorityQueue()
    unexplored.put((calculate_manhattan_distance(start, end), start))
    explored = {}
    explored[start] = None

    while not unexplored.empty():
        current = unexplored.get()
        current = current[1]
        if current == end:
            return explored
        for next_node in graph.neighbors(current):
            if next_node not in explored:
                unexplored.put((calculate_manhattan_distance(next_node, end), next_node))
                explored[next_node] = current
        g.draw_grid(current, explored, start, end)
        sys.stdout.write("\n")

    return explored


g = SquareGrid(30, 15)
g.walls = [(9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 3)]

parents = greedy_search(g, (8, 7), (25, 11))
# Visited, Start, End
g.draw_grid((-1, -1), parents, (8, 7), (25, 11))
