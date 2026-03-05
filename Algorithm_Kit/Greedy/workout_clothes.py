def workout_clothes(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    answer = n - len(lost_set)

    for num in sorted(lost_set):
        if num-1 in reserve_set:
            reserve_set.remove(num-1)
            answer += 1
        elif num+1 in reserve_set:
            reserve_set.remove(num+1)
            answer += 1

    return answer


print(workout_clothes(5, [2, 4], [1, 3, 5])) # result = 5
print(workout_clothes(5, [2, 4], [3])) # result = 4
print(workout_clothes(3, [3], [1])) # result = 2