def find_number_remain_is_one(n):
    answer = 2

    while answer < n:
        if n % answer == 1:
            return answer
        answer += 1

    return answer

print(find_number_remain_is_one(10)) # result = 3
print(find_number_remain_is_one(12)) # result = 11