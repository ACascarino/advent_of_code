import inspect
import pathlib

INPUT_FILE_NAME = "input.txt"
TEST_FILE_NAME = "test.txt"


def read_file(file_path: pathlib.Path) -> str:
    with open(file_path, "rt") as f:
        input = f.read()
    return input


def read_input(day_path: pathlib.Path) -> str:
    return read_file(day_path / INPUT_FILE_NAME)


def read_test(day_path: pathlib.Path) -> str:
    return read_file(day_path / TEST_FILE_NAME)


def here(extra_layers: int = 0) -> pathlib.Path:
    return pathlib.Path(inspect.stack()[1 + extra_layers].filename).absolute()


def day_dir(extra_layers: int = 0) -> pathlib.Path:
    return here(1 + extra_layers).parent.parent


def get_input() -> str:
    day_path = day_dir(extra_layers=1)
    return read_input(day_path)


def get_test() -> str:
    day_path = day_dir(extra_layers=1)
    return read_test(day_path)
