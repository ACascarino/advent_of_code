from part1 import DocumentPart1


class DocumentPart2(DocumentPart1):
    NUMBER_WORDS = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def replace_words_first_and_last(self, line: str) -> str:
        replaced = []

        # Build a list of `line` where the first occuring number word is 
        # replaced with a numeral, then the second, etc.
        for start in range(len(line)):
            for n_word, n_char in self.NUMBER_WORDS.items():
                if line.startswith(n_word, start):
                    replaced.append(line.replace(n_word, n_char))
                    break

        if len(replaced) == 0:
            # If replaced has no elements then there were no number words;
            # return the original string
            return line
        elif len(replaced) == 1:
            # If we have found one number word then return that replacement
            return replaced[0]
        else:
            # If we have found more than one number word, we can concatenate
            # the first and last strings. The first numeral remains the first
            # numeral, the last numeral remains the last numeral.
            return "".join([replaced[0], replaced[-1]])

    def process(self) -> int:
        numerified = map(self.replace_words_first_and_last, self.lines)
        translated = map(self.rm_alpha, numerified)
        relevant = map(self.get_relevant_chars, translated)
        converted = map(self.convert_to_num, relevant)
        return sum(converted)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read()

    print(DocumentPart2(input_file).process())
