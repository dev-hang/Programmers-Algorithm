def press_keypad(numbers, hand):
    answer = ''
    pad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2),
           '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    cur = [pad['*'], pad['#']]

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            cur[0] = pad[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            cur[1] = pad[num]
        else:
            left, right = cur[0], cur[1]
            left_dis = abs(left[0] - pad[num][0]) + abs(left[1] - pad[num][1])
            right_dis = abs(right[0] - pad[num][0]) + abs(right[1] - pad[num][1])

            if left_dis < right_dis or (left_dis == right_dis and hand == 'left'):
                answer += 'L'
                cur[0] = pad[num]
            elif left_dis > right_dis or (left_dis == right_dis and hand == 'right'):
                answer += 'R'
                cur[1] = pad[num]

    return answer



print(press_keypad([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))	# result = "LRLLLRLLRRL"
print(press_keypad([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))	# result = "LRLLRRLLLRR"
print(press_keypad([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))	# result = "LLRLLRLLRL"