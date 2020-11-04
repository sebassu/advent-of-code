result, lines = 0,  open("input.txt", "r").readlines()
for line in lines:
    d1, d2, d3 = sorted(int(part) for part in line.split('x'))
    result += 2 * (d1 + d2) + d1 * d2 * d3
print(f"{result} feet of ribbon are needed in total")
