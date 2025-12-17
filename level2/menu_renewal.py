from itertools import combinations

def menu_renewal(orders, course):
    result = [[] * (course[-1] + 1) for _ in range(course[-1] + 1)]
    dic = {}
    for num in course:
        for order in orders:
            combi = combinations(order, num)
            for c in combi:
                c = ''.join(sorted(c))
                if c not in dic:
                    dic[c] = 1
                else:
                    dic[c] += 1
    arr = []
    for k in dic:
        arr.append([k, dic[k]])
    arr.sort(key=lambda x: (len(x[0]), x[1]), reverse=True)
    m = 0
    for i, j in arr:
        if j >= max(2, m):
            result[len(i)].append(i)
            m = j

    answer = []
    for i in result:
        for j in i:
            answer.append(j)

    answer.sort()

    return answer





print(menu_renewal(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# result = ["AC", "ACDE", "BCFG", "CDE"]
print(menu_renewal(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# result = ["ACD", "AD", "ADE", "CD", "XYZ"]
print(menu_renewal(["XYZ", "XWY", "WXA"], [2,3,4]))
# result = ["WX", "XY"]