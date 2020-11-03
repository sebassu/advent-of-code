counter, instructions = 0, open("input.txt", "r").readline()
for character in instructions:
    counter += 1 if character == "(" else -1
print(f"Instructions took Santa to floor {counter}")
