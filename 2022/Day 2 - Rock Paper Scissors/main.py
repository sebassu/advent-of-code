from re import match

LOSS = 88
TIE = 89
WIN = 90
scores = [3, 6, 0]


def result_score_for(action: int, opponent_move: int = 86) -> int:
    return scores[(action - opponent_move) % 3]


def move_score_for(action: int, move: int) -> int:
    if action == LOSS: return (move - 66) % 3 + 1
    if action == TIE: return move - 64
    if action == WIN: return (move - 64) % 3 + 1


result1, result2 = 0, 0
for line in open("input.txt", "r").readlines():
    opponent_move, action = map(ord, match(r"([ABC]) ([XYZ])", line).groups())
    result1 += (action - 87) + result_score_for(action - 23, opponent_move)
    result2 += move_score_for(action, opponent_move) + result_score_for(action)
print(f"According to the rules for part 1, the result is {result1}.")
print(f"With the updated rules for part 2, the result is {result2}.")
