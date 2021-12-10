from functools import reduce


def check_line(line):
    brackets = []
    incorrect = []
    bracket_key = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }
    for c in line:
        if c in bracket_key.keys():
            brackets.append(c)
        else:
            closer = brackets.pop()
            if bracket_key[closer] != c:
                incorrect.append(c)
    return incorrect


scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
errors = []
with open('01.txt') as f:
    for item in f.readlines():
        errors.extend(check_line(item.strip()))
score = 0
for err in errors:
    score += scoring[err]
print('Part 1:', score)


def check_line_2(line):
    brackets = []
    bracket_key = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }
    for c in line:
        if c in bracket_key.keys():
            brackets.append(c)
        else:
            closer = brackets.pop()
            if bracket_key[closer] != c:
                return []
    return [bracket_key[x] for x in brackets[::-1]]


scoring = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
scores = []
with open('01.txt') as f:
    for item in f.readlines():
        if result := check_line_2(item.strip()):
            result.insert(0, 0)
            scores.append(reduce(lambda x, y: (x*5)+scoring[y], result))

print('Part 2:', sorted(scores)[len(scores)//2])
