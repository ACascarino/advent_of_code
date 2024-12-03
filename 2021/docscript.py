import advent_of_code_utils as aoc_utils
import shutil

folder_2021 = aoc_utils.here().parent
for subfolder in folder_2021.glob("day*"):
    if not (subfolder / "c").exists() or (subfolder / "py").exists():
        shutil.rmtree(subfolder)
