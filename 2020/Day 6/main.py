result, answers = 0, set()
for line in map(str.rstrip, open("input.txt", "r")):
    if line == "":
        result += len(answers)
        answers.clear()
    else:
        answers.update(line)
print(result + len(answers))
