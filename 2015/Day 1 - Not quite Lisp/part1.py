fileData = open("input.txt", "r")
for line in fileData.readlines():
    counter = 0
    for character in line:
        if character == "(":
            counter += 1
        else:
            counter -= 1
    print(f"Instructions took Santa to floor {counter}")
