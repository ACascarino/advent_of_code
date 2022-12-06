if __name__ == "__main__":
    with open("input.txt", "r") as file:
        puzzle_input = file.read()

    for position in range(len(puzzle_input)):
        sequence = puzzle_input[position : position + 4]
        if len(set(sequence)) == len(sequence):
            print(position + 4)
            break
