def all_unique(sequence):
    return len(set(sequence)) == len(sequence)


def find_unique_substring_of_length_x(sequence, length):
    for position in range(len(sequence)):
        substring = sequence[position : position + length]
        if all_unique(substring):
            return position


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    substring_start = find_unique_substring_of_length_x(puzzle_input, 4)
    print(substring_start + 4)
