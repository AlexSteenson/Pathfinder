from map import *
import Queue as Q


def calculate_manhattan_distance(start, end):
    (start_x, start_y) = start
    (end_x, end_y) = end
    return abs(start_x - end_x) + abs(start_y - end_y)


def a_star_search(graph, start, end):
    unexplored = Q.PriorityQueue()
    unexplored.put((calculate_manhattan_distance(start, end), start))
    found = {start: None}
    cost = {start: 0}

    while not unexplored.empty():
        current = unexplored.get()
        current = current[1]

        if current == end:
            break

        for next_node in graph.neighbors(current):

            tentative_gScore = cost[current] + 1
            if next_node not in found:
                cost[next_node] = sys.maxsize
                found[next_node] = current

            if cost[next_node] > tentative_gScore:
                cost[next_node] = tentative_gScore
                unexplored.put((calculate_manhattan_distance(next_node, end) + tentative_gScore, next_node))

        g.draw_grid(current, found, start, end)
        print('\n')
    return found


g = SquareGrid(30, 17)
#g.walls = [(9, 16), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 14), (9, 13), (9, 3), (9, 2), (9, 1), (9, 15)]
g.walls = [(9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 14), (9, 13), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (24, 12), (24, 11), (24, 10), (25, 10), (25, 12), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 10)]
begin = (0, 8)
goal = (25, 11)
parents = a_star_search(g, begin, goal)
path = g.reconstruct_path(parents, begin, goal)
g.draw_grid((-1, -1), path, begin, goal)
