from itertools import combinations

def candidate_key(relation):
    combis, result = [], []
    n = len(relation[0])

    for i in range(1, n + 1):
        for c in combinations(range(n), i):
            combis.append(c)

    for combi in combis:
        combi_set = set()

        for row in relation:
            unique = []
            for idx in combi:
                unique.append(row[idx])
            combi_set.add(tuple(unique))

        if len(combi_set) == len(relation):
            minimal = True
            for key in result:
                cnt = 0
                for column in key:
                    if column in combi:
                        cnt += 1
                if cnt == len(key):
                    minimal = False
            if minimal:
                result.append(combi)

    return len(result)




print(candidate_key([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# result = 2