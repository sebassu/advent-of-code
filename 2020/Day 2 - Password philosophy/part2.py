from re import match


def is_valid(string: str, character: str, position1: int, position2: int) -> bool:
    return (string[int(position1) - 1] == character) != (string[int(position2) - 1] == character)


result = 0
for line in open("input.txt", "r").readlines():
    position1, position2, character, string = match(
        r"^(\d+)-(\d+) (\w): (\w+)$", line).groups()
    result += 1 if is_valid(string, character, position1, position2) else 0
print(f"The total number of valid passwords is {result}")
