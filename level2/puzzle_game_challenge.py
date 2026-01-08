def puzzle_game_challenge(diffs, times, limit):
    min_level = min(diffs)
    max_level = max(diffs)

    while min_level <= max_level:
        lm = limit
        level = (min_level + max_level) // 2
        for i in range(len(diffs)):
            if diffs[i] <= level:
                lm -= times[i]
            else:
                lm -= (times[i] + times[i - 1]) * (diffs[i] - level) + times[i]

        if lm >= 0:
            max_level = level - 1
        else:
            min_level = level + 1

    return min_level


print(puzzle_game_challenge([1, 5, 3], [2, 4, 7], 30))
# result = 3
print(puzzle_game_challenge([1, 4, 4, 2], [6, 3, 8, 2], 59))
# result = 2
print(puzzle_game_challenge([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
# result = 294
print(puzzle_game_challenge([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))
# result = 39354

