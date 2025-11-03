def lotto_top_and_bottom(lottos, win_nums):
    answer = []
    win_cnt, zero_cnt = 0, 0
    order = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}

    for num in lottos:
        if num != 0 and num in win_nums:
            win_cnt += 1
        elif num == 0:
            zero_cnt += 1

    answer = [order.get(win_cnt + zero_cnt, 6), order.get(win_cnt, 6)]

    return answer



print(lotto_top_and_bottom([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))
# result = [3, 5]

print(lotto_top_and_bottom([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]))
# result = [1, 6]

print(lotto_top_and_bottom([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))
# result = [1, 1]
