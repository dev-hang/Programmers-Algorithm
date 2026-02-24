def collect_sticker(sticker):
    n = len(sticker)
    dp1 = [0] * (n-1)
    dp2 = [0] * (n-1)

    if n <= 2:
        return max(sticker)

    for i, num in enumerate(sticker[:-1]):
        dp1[i] = max(dp1[i-1], dp1[i-2] + num)

    for i, num in enumerate(sticker[1:]):
        dp2[i] = max(dp2[i-1], dp2[i-2] + num)

    return max(dp1[-1], dp2[-1])



print(collect_sticker([14, 6, 5, 11, 3, 9, 2, 10])) # result = 36
print(collect_sticker([1, 3, 2, 5, 4])) # result = 8