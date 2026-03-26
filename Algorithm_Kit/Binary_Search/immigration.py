def immigration(n, times):
    answer = 0
    left, right = min(times), max(times)*n

    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for time in times:
            cnt += mid//time
        if cnt >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1

    return answer



print(immigration(6, [7, 10])) # result = 28