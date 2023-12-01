CRATE_WIDTH = 3
CRATE_SPACE = 1
REMOVE_ALL_LOWERCASE = str.maketrans({chr(x):None for x in range(ord("a"), ord("z")+1)})

with open("input.txt", "r") as file:
    puzzle_input = file.read()

crates, instructions = (x.splitlines() for x in puzzle_input.split("\n\n"))
number_of_columns = max(map(int, crates.pop().replace(" ","")))
columns = {x+1:list() for x in range(number_of_columns)}

for line in crates:
    for column in range(1, number_of_columns + 1):
        crate_pointer = (column - 1) * (CRATE_WIDTH + CRATE_SPACE)
        crate = line[crate_pointer : crate_pointer + CRATE_WIDTH]
        if "[" in crate:
            crate_letter = crate[CRATE_WIDTH // 2]
            columns[column].insert(0, crate_letter)

for line in instructions:
    quantity, source, dest = map(int, line.translate(REMOVE_ALL_LOWERCASE).split())
    columns[dest] += columns[source][-quantity :]
    del columns[source][-quantity :]

top_crates = [x[-1] for x in columns.values()]
print("".join(top_crates))