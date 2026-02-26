def jewelry_shopping(gems):
    n, m = len(gems), len(set(gems))
    start, end = 0, 0
    answer = [0, n-1]
    dic = {gems[0]: 1}

    while start < n and end < n:
        if len(dic) < m:
            end += 1
            if end == n:
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if end-start < answer[1]-answer[0]:
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

    answer[0] += 1
    answer[1] += 1

    return answer






print(jewelry_shopping(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # result = [3, 7]
print(jewelry_shopping(["AA", "AB", "AC", "AA", "AC"])) # result = [1, 3]
print(jewelry_shopping(["XYZ", "XYZ", "XYZ"])) # result = [1, 1]
print(jewelry_shopping(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # result = [1, 5]