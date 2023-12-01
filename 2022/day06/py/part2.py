import part1

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    substring_start = part1.find_unique_substring_of_length_x(puzzle_input, 14)
    print(substring_start + 14)
