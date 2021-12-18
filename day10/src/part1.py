CHAR_VALUES = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137 
}

OPENING_BRACE = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}

with open("input.txt") as f:
    input_lines = [x.strip() for x in f.readlines()]

result = 0
for line in input_lines:
    chunks = []
    priority = 1
    corrupt = False
    for character in line:
        if character in ('(', '[', '<', '{'):
            chunks.append((character,priority))
            priority += 1
        elif character in (')', ']', '>', '}'):
            priority -=1
            target = [k for k,v in chunks if k == OPENING_BRACE[character] and v == priority]
            if not target:
                corrupt = True
                result += CHAR_VALUES[character]
                break
            else:
                chunks.remove((OPENING_BRACE[character], priority))
print(result)