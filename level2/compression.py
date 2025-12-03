def compression(msg):
    answer = []
    dic = {chr(64 + i): i for i in range(1, 27)}
    j = 0
    while j < len(msg):
        for i in range(len(msg) + 1, 0, -1):
            if msg[j:i] in dic:
                answer.append(dic[msg[j:i]])
                if msg[i:i + 1]:
                    dic[msg[j:i + 1]] = len(dic) + 1
                j = i - 1
                break
        j += 1

    return answer


print(compression('KAKAO')) # result = [11, 1, 27, 15]
print(compression('TOBEORNOTTOBEORTOBEORNOT')) # result = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(compression('ABABABABABABABAB')) # result = [1, 2, 27, 29, 28, 31, 30]

