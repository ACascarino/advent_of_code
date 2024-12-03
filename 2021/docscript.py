import advent_of_code_utils as aoc_utils
import os

folder_2021 = aoc_utils.here().parent
for subfolder in folder_2021.glob("day*"):
    if (subfolder / "c").exists() and (subfolder / "c").glob("*.py") is not None:
        os.rmdir(subfolder / "c")
