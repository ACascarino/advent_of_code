class DocumentPart1:
    ALPHA_REMOVE_TABLE = str.maketrans(
        "", "", "".join([chr(x) for x in range(ord("a"), ord("Z")+1)])
    )

    def __init__(self, text: str) -> None:
        self.lines = text.splitlines()

    def rm_alpha(self, line: str) -> str:
        return line.translate(self.ALPHA_REMOVE_TABLE)

    def get_relevant_chars(self, line: str) -> str:
        return "".join([line[0], line[-1]])

    def convert_to_num(self, line: str) -> int:
        return int(line)

    def process(self) -> int:
        translated = map(self.rm_alpha, self.lines)
        relevant = map(self.get_relevant_chars, translated)
        converted = map(self.convert_to_num, relevant)
        return sum(converted)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read()

    print(DocumentPart1(input_file).process())
