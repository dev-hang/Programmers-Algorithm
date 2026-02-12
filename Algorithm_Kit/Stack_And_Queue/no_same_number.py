def no_same_number(arr):
    answer = []

    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)

    return answer





print(no_same_number([1,1,3,3,0,1,1])) # result = [1,3,0,1]
print(no_same_number([4,4,4,3,3])) # result = [4,3]