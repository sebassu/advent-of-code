fileData = open("input.txt", "r")
for line in fileData.readlines():
    counter = 0
    for position, character in enumerate(line):
        if character == "(":
            counter += 1
        else:
            counter -= 1
        if counter == -1:
            print("Santa first entered the basement at position",
                  f"{position + 1}")
            break
