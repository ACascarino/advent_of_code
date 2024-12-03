import collections
import pathlib

here = pathlib.Path(__file__).absolute()


def app(input_path: pathlib.Path):
    with open(input_path, "rt") as f:
        input = f.read()
    lines = (line.strip() for line in input.splitlines())
    left, right = zip(*(line.split() for line in lines))
    r_counts = collections.Counter(right)
    l_sum = sum(int(i) * r_counts[i] for i in left)
    print("\n", l_sum)


if __name__ == "__main__":
    app(here.parent.parent / "input.txt")
