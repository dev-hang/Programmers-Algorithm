from itertools import combinations

def search_rankings(info, query):
    answer = []
    com = {}

    for data in info:
        data = data.split()
        cases = []
        for i in range(5):
            for combi in combinations([0,1,2,3], i):
                case = ''
                for j in range(4):
                    if j in combi:
                        case += data[j]
                    else:
                        case += '-'
                cases.append(case)
        for case in cases:
            if case in com.keys():
                com[case].append(int(data[4]))
            else:
                com[case] = [int(data[4])]

    for key in com.keys():
        com[key].sort()

    for q in query:
        a, b, c, d = q.split(' and ')
        d, e = d.split()
        case = a + b + c + d

        if case in com.keys():
            target = com[case]
            min_score, max_score = 0, len(target)

            while min_score < max_score:
                mid = (min_score + max_score) // 2
                if target[mid] >= int(e):
                    max_score = mid
                else:
                    min_score = mid + 1

            answer.append(len(target) - max_score)
        else:
            answer.append(0)

    return answer




print(search_rankings(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
                      ,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# result = [1,1,1,1,2,4]