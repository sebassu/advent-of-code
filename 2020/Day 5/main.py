from math import floor, ceil

result = 0
for line in open("input.txt", "r").readlines():
    rows, columns = (0, 127), (0, 7)
    for instruction in line[:7]:
        rowsHalf = sum(rows) / 2
        rows = (ceil(rowsHalf), rows[1]) if instruction == "B" \
            else (rows[0], floor(rowsHalf))
    for instruction in line[-3:]:
        columnsHalf = sum(columns) / 2
        columns = (ceil(columnsHalf), columns[1]) if instruction == "R" \
            else (columns[0], floor(columnsHalf))
    if rows[1] * 8 + columns[1] == 914:
        print(line)
    result = max(result, (rows[1] * 8) + columns[1])
print(result)


result = 0
for line in map(str.rstrip, open("input.txt", "r").readlines()):
    seatID = int("".join('1' if x == 'B' or
                         x == 'R' else '0' for x in line), 2)
    result = max(result, seatID)
print(f"The maximum seat ID found was {result}")
