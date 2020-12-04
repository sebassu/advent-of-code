xStep = 3

x, result = 0, 0
for index, line in enumerate(open("input.txt", "r").readlines()):
    result += 1 if line[x] == '#' else 0
    x = (x + xStep) % (len(line) - 1)
print(f"Tree count found was {result}")
