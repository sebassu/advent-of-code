totalCalories, currentCalories = [], 0
for line in open("input.txt", "r").readlines():
    if line != "\n": currentCalories += int(line)
    else:
        totalCalories.append(currentCalories)
        currentCalories = 0
print(f"The elf with the most calories had {max(totalCalories)} calories.")
print(f"The three elves with the most calories are carrying \
{sum(sorted(totalCalories, reverse=True)[:3])} calories in total.")
