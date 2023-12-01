class Graph:
    def __init__(self, puzzle_input: str) -> None:
        lines = puzzle_input.splitlines()

        self.grid_height = len(lines)
        self.grid_width = len(lines[0])

        self.vertices = {
            (xidx, yidx): Vertex(self, char, xidx, yidx)
            for yidx, line in enumerate(lines)
            for xidx, char in enumerate(line)
        }
        for vertex in self.vertices.values():
            if vertex.value == ord("S"):
                self.start_vertex = vertex
                vertex.value = ord("a")
            elif vertex.value == ord("E"):
                self.end_vertex = vertex
                vertex.value = ord("z")

        for vertex in self.vertices.values():
            for neighbour in [
                (self.vertices[coords]) for coords in vertex.neighbouring_coords
            ]:
                if vertex.value - neighbour.value >= -1:
                    vertex.adjacencies.append(neighbour)

    def h(self, vertex1, vertex2):
        return vertex2.value - vertex1.value

    def find_shortest_path(self):
        def reconstruct_path(came_from, current):
            total_path = [current]
            while current in came_from:
                current = came_from[current]
                total_path.append(current)
            total_path = list(reversed(total_path))
            return total_path

        open_set = {self.start_vertex}
        came_from = dict()
        g_score = {x: 16031996 for x in self.vertices.values()}
        g_score[self.start_vertex] = 0
        f_score = {x: 16031996 for x in self.vertices.values()}
        f_score[self.start_vertex] = self.h(self.start_vertex, self.end_vertex)

        while open_set:
            current = min(open_set, key=f_score.get)
            if current is self.end_vertex:
                return reconstruct_path(came_from, current)

            open_set.remove(current)
            for neighbour in current.adjacencies:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = tentative_g_score
                    f_score[neighbour] = tentative_g_score + self.h(
                        neighbour, self.end_vertex
                    )
                    if neighbour not in open_set:
                        open_set.add(neighbour)
        return None


class Vertex:
    def __init__(self, parent: Graph, value: str, x: int, y: int) -> None:
        self.graph = parent
        self.value = ord(value)
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.adjacencies = list()
        self.neighbouring_coords = (
            x
            for x in (
                self.up_coords,
                self.down_coords,
                self.left_coords,
                self.right_coords,
            )
            if x is not None
        )

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}): {chr(self.value)}"

    @property
    def up_coords(self):
        return (self.x, self.y - 1) if self.y != 0 else None

    @property
    def down_coords(self):
        return (self.x, self.y + 1) if self.y != (self.graph.grid_height - 1) else None

    @property
    def left_coords(self):
        return (self.x - 1, self.y) if self.x != 0 else None

    @property
    def right_coords(self):
        return (self.x + 1, self.y) if self.x != (self.graph.grid_width - 1) else None


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

mountain = Graph(puzzle_input)
path = mountain.find_shortest_path()
print(len(path) - 1)
