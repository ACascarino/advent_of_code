class Cd:
    def __init__(self, target: str) -> None:
        self.target = target


class Ls:
    def __init__(self, result: list[str]) -> None:
        self.result = result


class ConsoleOutput:
    def __init__(self, console: str) -> None:
        self.console = console.splitlines()

    def __iter__(self) -> str:
        for line_idx, line in enumerate(self.console):
            if line.startswith("$"):
                if (cd_start := line.find("cd")) != -1:
                    yield Cd(line[cd_start + 3 :])
                elif (line.find("ls")) != -1:
                    yield Ls(self.get_next_noncommand_lines(line_idx))

    def get_next_noncommand_lines(self, start_idx):
        result = list()
        num_commands = len(self.console)
        while True:
            if start_idx + 1 < num_commands:
                return_line = self.console[start_idx + 1]
                if not return_line.startswith("$"):
                    result.append(return_line)
                    start_idx += 1
                else:
                    break
            else:
                break
        return result


class DirectoryTree:
    def __init__(self) -> None:
        self.root = Directory("/")

    def evaluate_dir_sizes(self) -> None:
        _ = self.root.size

    def query(self, node_type, querying, operation, value):
        if querying != "size":
            raise NotImplementedError
        if operation != "<=":
            raise NotImplementedError
        if node_type != "directory":
            raise NotImplementedError

        return self.root.query(node_type, querying, operation, value)


class Console:
    def __init__(self, tree: DirectoryTree) -> None:
        self.tree = tree
        self.cwd = tree.root

    # Assumption: we need to know a directory exists before we cd to it; go to root if we get an invalid one
    def process_commands(self, commands: ConsoleOutput):
        for command in commands:
            if type(command) == Cd:
                if command.target == "/":
                    self.cwd = self.tree.root
                else:
                    self.cwd = self.cwd.parse_cd(command.target)
                if self.cwd is None:
                    self.cwd = self.tree.root
            elif type(command) == Ls:
                self.cwd.add_children(command.result)


class Directory:
    def __init__(self, name: str, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.children = {}
        self._computed_size = None

    def __repr__(self) -> str:
        return self.name

    @property
    def size(self) -> int:
        if self._computed_size is None:
            self._computed_size = self._compute_size()
        return self._computed_size

    def _compute_size(self) -> int:
        if len(self.children) == 0:
            return 0
        else:
            return sum(child.size for child in self.children.values())

    def add_children(self, new_children: list[str]):
        for child in new_children:
            part1, part2 = child.split()
            if part1 == "dir":
                self.children |= {part2: Directory(name=part2, parent=self)}
            else:
                self.children |= {part2: FileObject(name=part2, size=int(part1))}

    def parse_cd(self, target):
        if target == "..":
            return self.parent
        else:
            return self.children.get(target, None)

    def query(self, node_type, querying, operation, value):
        # I want this to return [ ... ], all subobjects that match the query
        # Run query on self, run query on children, amalgamate the results
        # This should always return a flat list, which means child_results should always only be a list of lists.

        if node_type == "directory" and querying == "size" and operation == "<=":
            self_results = (
                child
                for child in self.children.values()
                if child.size <= value and type(child) == Directory
            )
            child_results = (
                child.query(node_type, querying, operation, value)
                for child in self.children.values()
                if type(child) == Directory
            )

            results = []
            results.extend(self_results)
            results.extend(
                inner
                for result in child_results
                if result is not None
                for inner in result
            )

            # print(self.name, self_results, child_results, results if results else None)
            return results if results else None


class FileObject:
    def __init__(self, name: str, size: int = 0) -> None:
        self.name = name
        self.size = size


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    file_directory = DirectoryTree()
    commands = ConsoleOutput(puzzle_input)
    working_console = Console(file_directory)

    working_console.process_commands(commands)

    results = file_directory.query("directory", "size", "<=", 100000)
    print(sum(result.size for result in results))
