def estimated_match_sheet(n,a,b):
    answer = 0

    while a != b:
        a, b = (a+1)//2, (b+1)//2
        answer += 1
        
    return answer


print(estimated_match_sheet(8, 4, 7)) # result = 3