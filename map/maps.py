import sys


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, node_id):
        (x, y) = node_id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, node_id):
        return node_id not in self.walls

    def neighbors(self, node_id):
        (x, y) = node_id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse()  # aesthetics

        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

    def draw_grid(self, current, visited, start, end):
        for y in range(self.height):
            for x in range(self.width):
                draw_node = (x, y)

                if draw_node in self.walls:
                    sys.stdout.write(" # ")
                elif draw_node == current:
                    sys.stdout.write(" C ")
                elif draw_node == start:
                    sys.stdout.write(" S ")
                elif draw_node == end:
                    sys.stdout.write(" E ")
                elif draw_node in visited:
                    sys.stdout.write(" V ")
                else:
                    sys.stdout.write(" . ")
            sys.stdout.write("\n")
