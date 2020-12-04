from typing import Iterable

slopes = [(x, 1) for x in [1, 3, 5, 7]] + [(1, 2)]
lines = open("input.txt", "r").readlines()


def traverse_map_with(xStep: int, yStep: int, lines: Iterable[str]) -> int:
    x, trees = 0, 0
    for y in range(0, len(lines), yStep):
        trees += 1 if lines[y][x] == '#' else 0
        x = (x + xStep) % (len(lines[y]) - 1)
    print(f"Tree count found with slope ({xStep}, {yStep}) was {trees}")
    return trees


result = 1
for xStep, yStep in slopes:
    result *= traverse_map_with(xStep, yStep, lines)
print(f"The total multiplication result is {result}")
