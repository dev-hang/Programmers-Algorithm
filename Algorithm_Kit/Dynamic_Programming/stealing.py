def stealing(money):
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]

    dp1[0] = dp1[1] = money[0]
    dp2[0], dp2[1] = 0, money[1]

    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(max(dp1), max(dp2))



print(stealing([1, 2, 3, 1])) # result = 4