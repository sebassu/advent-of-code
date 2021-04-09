result,  answers, totalPeople = 0, {}, 0
for line in map(str.rstrip, open("input.txt", "r")):
    if line == "":
        result += len([answer for answer, count in answers.items()
                       if count == totalPeople])
        totalPeople = 0
        answers.clear()
    else:
        totalPeople += 1
        for answer in line:
            if answer in answers:
                answers[answer] += 1
            else:
                answers[answer] = 1
print(result)
