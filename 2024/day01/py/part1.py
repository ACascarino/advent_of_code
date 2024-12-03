import pathlib

here = pathlib.Path(__file__).absolute()


def app(input_path: pathlib.Path):
    with open(input_path, "rt") as f:
        input = f.read()
    lines = (line.strip() for line in input.splitlines())
    left, right = zip(*(line.split() for line in lines))
    diffs = (abs(int(l) - int(r)) for l, r in zip(sorted(left), sorted(right)))
    print("\n", sum(diffs))


if __name__ == "__main__":
    app(here.parent.parent / "input.txt")
