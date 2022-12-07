import operator
import itertools


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


class FileObject:
    def __init__(self, name: str, size: int = None) -> None:
        self.name = name
        self._computed_size = size

    def __repr__(self) -> str:
        return self.name

    @property
    def size(self) -> int:
        if self._computed_size is None:
            self._computed_size = self._compute_size()
        return self._computed_size

    def _compute_size(self) -> int:
        try:
            return sum(child.size for child in self.children.values())
        except AttributeError:
            raise NotImplementedError


class Directory(FileObject):
    def __init__(self, name: str, parent=None) -> None:
        super().__init__(name)
        self.parent = parent
        self.children = {}

    def add_children(self, new_children: list[str]):
        for child in new_children:
            p1, p2 = child.split()
            if p1 == "dir":
                self.children |= {p2: Directory(name=p2, parent=self)}
            else:
                self.children |= {p2: FileObject(name=p2, size=int(p1))}

    def parse_cd(self, target):
        if target == "..":
            return self.parent
        else:
            return self.children.get(target, self)

    def query(self, node_type, querying, operation, value):
        self_results = (
            child
            for child in self.children.values()
            if operation(getattr(child, querying), value)
            and isinstance(child, node_type)
        )
        child_results = (
            child.query(node_type, querying, operation, value)
            for child in self.children.values()
            if isinstance(child, Directory)
        )

        results = itertools.chain(
            self_results,
            (inner for result in child_results for inner in result),
        )

        return results


class Console:
    def __init__(self, root: Directory) -> None:
        self.root = root
        self.cwd = root

    def process_commands(self, commands: ConsoleOutput):
        for command in commands:
            if isinstance(command, Cd):
                if command.target == "/":
                    self.cwd = self.root
                else:
                    self.cwd = self.cwd.parse_cd(command.target)
            elif isinstance(command, Ls):
                self.cwd.add_children(command.result)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    root = Directory("/")
    commands = ConsoleOutput(puzzle_input)
    working_console = Console(root)

    working_console.process_commands(commands)

    total_space = 70000000
    required_space = 30000000
    filesystem_use = root.size
    extra_space = required_space - (total_space - filesystem_use)

    part_1_results = root.query(Directory, "size", operator.le, 100000)
    part_2_results = root.query(Directory, "size", operator.ge, extra_space)
    print("Part 1:", sum(result.size for result in part_1_results))
    print("Part 2:", min(result.size for result in part_2_results))
