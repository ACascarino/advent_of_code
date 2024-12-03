import advent_of_code_utils as aoc_utils
import shutil

folder_2021 = aoc_utils.here().parent
for subfolder in folder_2021.glob("day*"):
    if (subfolder / "c").exists():
        if not sorted((subfolder / "c").glob("*.py")) == []:
            shutil.rmtree(subfolder / "c")
