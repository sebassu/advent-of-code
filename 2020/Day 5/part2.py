from math import floor, ceil

maximum, minimum, suma = 0, 0, 0
for line in map(str.rstrip, open("input.txt", "r")):
    seatID = int("".join('1' if x == 'B' or
                         x == 'R' else '0' for x in line), 2)
    suma += seatID
    maximum = max(maximum, seatID)
    minimum = min(minimum, seatID)
