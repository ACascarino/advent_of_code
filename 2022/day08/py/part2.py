directions = (NORTH, WEST, EAST, SOUTH) = (0, 1, 2, 3)


class Forest:
    def __init__(self, forest: str) -> None:
        split_forest = forest.splitlines()
        self.east_west = list()
        self.north_south = [list() for _ in range(len(split_forest))]
        for idx, line in enumerate(forest.splitlines()):
            self.east_west.append(list(map(Tree, line)))
            for bidx, elem in enumerate(self.east_west[idx]):
                self.north_south[bidx].append(elem)
        self.map_neighbours()

    def map_neighbours(self):
        for lidx, line in enumerate(self.east_west):
            for tidx, tree in enumerate(line):
                if tidx != 0:
                    tree.neighbours[WEST] = line[tidx - 1]
                if tidx != len(line) - 1:
                    tree.neighbours[EAST] = line[tidx + 1]
                if lidx != 0:
                    tree.neighbours[NORTH] = self.east_west[lidx - 1][tidx]
                if lidx != len(self.east_west) - 1:
                    tree.neighbours[SOUTH] = self.east_west[lidx + 1][tidx]

    def fire_lazors(self, from_direction) -> None:
        reverse_directions = (
            True if from_direction == EAST or from_direction == SOUTH else False
        )
        target_iterable = (
            self.east_west
            if from_direction == EAST or from_direction == WEST
            else self.north_south
        )
        for line in target_iterable:
            line = reversed(line) if reverse_directions else line
            tree_height = -1
            for tree in line:
                if tree.value > tree_height:
                    tree.visibility[from_direction] = True
                    tree_height = tree.value

    def fire_all_lazors(self):
        _ = [self.fire_lazors(d) for d in directions]

    def visibility_matrix(self):
        return [[t.visible() for t in x] for x in self.east_west]

    def score_all_trees(self):
        for line in self.east_west:
            for tree in line:
                tree.score = [self.score_direction(tree, d) for d in directions]

    def score_direction(self, tree, direction):
        score = 0
        neighbour = tree.neighbours[direction]
        while neighbour is not None:
            score += 1
            if neighbour.value >= tree.value:
                break
            else:
                neighbour = neighbour.neighbours[direction]
        return score


class Tree:
    def __init__(self, value: str) -> None:
        self.value = int(value)
        self.visibility = [False, False, False, False]
        self.score = [0, 0, 0, 0]
        self.neighbours = [None, None, None, None]

    def __repr__(self) -> str:
        return str(self.value)

    def visible(self) -> bool:
        return any(self.visibility)

    def get_total_score(self) -> int:
        return self.score[0] * self.score[1] * self.score[2] * self.score[3]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    patch = Forest(puzzle_input)
    patch.score_all_trees()

    print(max(t.get_total_score() for row in patch.east_west for t in row))
