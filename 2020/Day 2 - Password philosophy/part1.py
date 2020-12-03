from re import match


def is_valid(string: str, character: str, minimum: int, maximum: int) -> bool:
    ocurrences = string.count(character)
    return ocurrences >= int(minimum) and ocurrences <= int(maximum)


result = 0
for line in open("input.txt", "r").readlines():
    minimum, maximum, character, string = match(
        r"^(\d+)-(\d+) (\w): (\w+)$", line).groups()
    result += 1 if is_valid(string, character,
                            int(minimum), int(maximum)) else 0
print(f"The total number of valid passwords is {result}")
