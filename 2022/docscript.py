from pathlib import Path
import advent_of_code_utils as aoc_utils
import shutil

folder_2022 = aoc_utils.here().parent
for child in folder_2022.rglob("**/day*"):
    newpydir = child / "py"
    newcppdir = child / "cpp"

    shutil.rmtree(newcppdir)
    (child / "CMakeLists.txt").unlink()
