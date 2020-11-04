result, lines = 0,  open("input.txt", "r").readlines()
for line in lines:
    d1, d2, d3 = sorted(int(part) for part in line.split('x'))
    result += 2 * d3 * (d1 + d2) + 3 * d1 * d2
print(f"{result} square feet of wrapping paper are needed in total")
