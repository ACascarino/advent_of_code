import part1


class Part2DirectoryTree(part1.DirectoryTree):
    def __init__(self) -> None:
        super().__init__()
        self.root = Part2Directory("/")

    def query(self, node_type, querying, operation, value):
        try:
            super().query(node_type, querying, operation, value)
        except NotImplementedError:
            if operation == ">=":
                return self.root.query(node_type, querying, operation, value)


class Part2Directory(part1.Directory):
    def __init__(self, name: str, parent=None) -> None:
        super().__init__(name, parent)

    def add_children(self, new_children: list[str]):
        for child in new_children:
            p1, p2 = child.split()
            if p1 == "dir":
                self.children |= {p2: Part2Directory(name=p2, parent=self)}
            else:
                self.children |= {p2: part1.FileObject(name=p2, size=int(p1))}

    def query(self, node_type, querying, operation, value):
        result = super().query(node_type, querying, operation, value)
        if result is not None:
            return result
        else:
            if node_type == "directory" and querying == "size" and operation == ">=":
                self_results = list(
                    child
                    for child in self.children.values()
                    if child.size >= value and isinstance(child, part1.Directory)
                )
                child_results = list(
                    child.query(node_type, querying, operation, value)
                    for child in self.children.values()
                    if isinstance(child, part1.Directory)
                )

                results = []
                results.extend(self_results)
                results.extend(
                    inner
                    for result in child_results
                    if result is not None
                    for inner in result
                )

                print(
                    self.name, self_results, child_results, results if results else None
                )
                return results if results else None


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    file_directory = Part2DirectoryTree()
    commands = part1.ConsoleOutput(puzzle_input)
    working_console = part1.Console(file_directory)

    working_console.process_commands(commands)

    total_space = 70000000
    required_space = 30000000
    filesystem_use = file_directory.root.size
    current_free_space = total_space - filesystem_use
    required_new_space = required_space - current_free_space

    results = file_directory.query("directory", "size", ">=", required_new_space)

    print(min(result.size for result in results))
