def input_split_int(puzzle_input:str) -> list[list[int]]:
    """
    "1 2 3 4\n5 6 7 8\n9 10 11 12" -> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    """
    return [[int(x) for x in line.strip().split()] for line in puzzle_input.splitlines()]