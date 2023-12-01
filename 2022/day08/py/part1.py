directions = (NORTH, EAST, SOUTH, WEST) = (0, 1, 2, 3)


class Forest:
    def __init__(self, forest: str) -> None:
        split_forest = forest.splitlines()
        self.east_west = list()
        self.north_south = [list() for _ in range(len(split_forest))]
        for idx, line in enumerate(forest.splitlines()):
            self.east_west.append(list(map(Tree, line)))
            for bidx, elem in enumerate(self.east_west[idx]):
                self.north_south[bidx].append(elem)

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


class Tree:
    def __init__(self, value: str) -> None:
        self.value = int(value)
        self.visibility = [False, False, False, False]

    def __repr__(self) -> str:
        return str(self.value)

    def visible(self) -> bool:
        return any(self.visibility)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    patch = Forest(puzzle_input)
    patch.fire_all_lazors()

    print(sum(x for y in patch.visibility_matrix() for x in y))
