counter, instructions = 0, open("input.txt", "r").readline()
for position, character in enumerate(instructions):
    counter += 1 if character == "(" else -1
    if counter == -1:
        print(f"Santa first entered the basement at position {position + 1}")
        break
