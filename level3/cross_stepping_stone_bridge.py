def cross_stepping_stone_bridge(stones, k):
    left, right = 1, max(stones) + 1

    while left < right - 1:
        mid = (left + right) // 2
        cnt = 0
        flg = True
        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                flg = False
                break
        if flg:
            left = mid
        else:
            right = mid

    return left


print(cross_stepping_stone_bridge([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
# result = 3
