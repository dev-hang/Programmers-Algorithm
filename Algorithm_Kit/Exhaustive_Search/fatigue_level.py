from itertools import permutations

def fatigue_level(k, dungeons):
    answer = []
    for case in permutations([i for i in range(len(dungeons))], len(dungeons)):
        cur, cnt = k, 0
        for i in case:
            if cur >= dungeons[i][0]:
                cur -= dungeons[i][1]
                cnt += 1
        answer.append(cnt)

    return max(answer)





print(fatigue_level(80, [[80,20],[50,40],[30,10]])) # result = 3