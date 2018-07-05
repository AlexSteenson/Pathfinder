from map import *
import Queue as Q


def breadth_first_search(graph, start, end):
    unexplored = Q.Queue()
    unexplored.put(start)
    found = {start: None}

    # While there are nodes still to be evaluated
    while not unexplored.empty():
        # Get the next node
        current = unexplored.get()
        # If the goal has been found stop
        if current == end:
            break

        # Get the neighbours of the current node
        for next_node in graph.neighbors(current):
            # If not yet found, add to the unexplored queue
            if next_node not in found:
                unexplored.put(next_node)
                found[next_node] = current

        # Printing code
        g.draw_grid(current, found, start, end)
        sys.stdout.write("\n")

    return found


g = SquareGrid(30, 15)
g.walls = [(9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 14), (9, 13), (9, 3)]
begin = (8, 7)
goal = (25, 11)
parents = breadth_first_search(g, begin, goal)
path = g.reconstruct_path(parents, begin, goal)
# Visited, Start, End
g.draw_grid((-1, -1), path, (8, 7), (25, 11))
