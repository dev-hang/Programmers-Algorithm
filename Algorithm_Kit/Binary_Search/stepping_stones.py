def stepping_stones(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    left, right = 0, rocks[-1]

    while left <= right:
        cnt, cur = 0, 0
        mid = (left + right) // 2
        for rock in rocks:
            dist = rock - cur
            if dist < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                cur = rock
        if cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer


print(stepping_stones(25, [2, 14, 11, 21, 17], 2))  # result = 4
