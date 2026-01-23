from itertools import product

def archery_competiton(n, info):
    answer = [-1]
    max_d = 0
    info.reverse()

    for game in product((True, False), repeat=11):
        s = sum(info[i]+1 for i in range(11) if game[i])

        if s <= n:
            apeach = sum(i for i in range(11) if not game[i] and info[i])
            ryan = sum(i for i in range(11) if game[i])
            d = ryan - apeach

            if d > max_d:
                max_d = d
                answer = [info[i]+1 if game[i] else 0 for i in range(11)]
                answer[0] += n-s

    answer.reverse()
    return answer


print(archery_competiton(5, [2,1,1,1,0,0,0,0,0,0,0])) # result = [0,2,2,0,1,0,0,0,0,0,0]
print(archery_competiton(1, [1,0,0,0,0,0,0,0,0,0,0])) # result = [-1]
print(archery_competiton(9, [0,0,1,2,0,1,1,1,1,1,1])) # result = [1,1,2,0,1,2,2,0,0,0,0]
print(archery_competiton(10, [0,0,0,0,0,0,0,0,3,4,3])) # result = [1,1,1,1,1,1,1,1,0,0,2]