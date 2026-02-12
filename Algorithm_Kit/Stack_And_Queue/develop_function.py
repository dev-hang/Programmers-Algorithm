from math import ceil

def develop_function(progresses, speeds):
    answer, time = [], []

    for i in range(len(progresses)):
        time.append(ceil((100-progresses[i])/speeds[i]))

    cnt = 1
    primary = time.pop(0)

    while time:
        secondary = time.pop(0)
        if primary >= secondary:
            cnt += 1
        else:
            answer.append(cnt)
            primary = secondary
            cnt = 1

    answer.append(cnt)

    return answer



print(develop_function([93, 30, 55], [1, 30, 5])) # result = [2, 1]
print(develop_function([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # result = [1, 3, 2]