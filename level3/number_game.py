def number_game(A, B):
    answer = 0
    A.sort()
    B.sort()
    for a in A:
        while B:
            b = B.pop(0)
            if a < b:
                answer += 1
                break
    return answer




print(number_game([5,1,3,7], [2,2,6,8])) # result = 3
print(number_game([2,2,2,2], [1,1,1,1])) # result = 0