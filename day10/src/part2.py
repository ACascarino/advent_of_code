CHAR_VALUES = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4 
}

CLOSING_BRACE = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

OPENING_BRACE = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}

def score(completion:str):
    total = 0
    for character in completion:
        total *= 5
        total += CHAR_VALUES[character]
    return total

def median(collection:list):
    n = len(collection)
    idx = (n // 2)
    return sorted(collection)[idx]


if __name__ == "__main__":
    with open("input.txt") as f:
        input_lines = [x.strip() for x in f.readlines()]

    scores = []
    for line in input_lines:
        chunks = []
        priority = 1
        corrupt = False
        for character in line:
            if character in OPENING_BRACE.values():
                chunks.append((character,priority))
                priority += 1
            elif character in CLOSING_BRACE.values():
                priority -=1
                target = [k for k,v in chunks if k == OPENING_BRACE[character] and v == priority]
                if not target:
                    corrupt = True
                    break
                else:
                    chunks.remove((OPENING_BRACE[character], priority))

        if not corrupt:
            completion = "".join(reversed([CLOSING_BRACE[character] for character, _ in chunks]))
            scores.append(score(completion))

    print(median(scores))