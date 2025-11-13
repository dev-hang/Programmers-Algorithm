def most_received_gifts(friends, gifts):
    n = len(friends)
    answer = [0] * n
    gift_idx = [0] * n
    table = [[0] * n for _ in range(n)]
    idx_dic = {}

    for i in range(n):
        idx_dic[friends[i]] = i

    for gift in gifts:
        give, get = gift.split()
        i, j = idx_dic[give], idx_dic[get]
        gift_idx[i] += 1
        gift_idx[j] -= 1
        table[i][j] += 1

    for i in range(n):
        for j in range(n):
            if i == j: continue
            if table[i][j] > table[j][i]:
                answer[i] += 1
            elif table[i][j] == table[j][i]:
                if gift_idx[i] > gift_idx[j]:
                    answer[i] += 1

    return max(answer)




print(most_received_gifts(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
# result = 2
print(most_received_gifts(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
# result = 4
print(most_received_gifts(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))
# result = 0