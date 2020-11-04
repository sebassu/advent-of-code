positions, nextMover = [[0, 0], [0, 0]], False
housesVisited, instructions = {"0,0"}, open("input.txt", "r").readline()
for move in instructions:
    if move == '^':
        positions[nextMover][1] += 1
    elif move == 'v':
        positions[nextMover][1] -= 1
    elif move == '<':
        positions[nextMover][0] -= 1
    else:
        positions[nextMover][0] += 1
    housesVisited.add(f"{positions[nextMover][0]},{positions[nextMover][1]}")
    nextMover = not nextMover
print(f"{len(housesVisited)} houses recieved presents that year")
