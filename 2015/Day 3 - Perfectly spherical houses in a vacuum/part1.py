currentX, currentY = 0, 0
housesVisited, instructions = {"0,0"}, open("input.txt", "r").readline()
for move in instructions:
    if move == '^':
        currentY += 1
    elif move == 'v':
        currentY -= 1
    elif move == '<':
        currentX -= 1
    else:
        currentX += 1
    housesVisited.add(f"{currentX},{currentY}")
print(f"Santa visited {len(housesVisited)} houses")
