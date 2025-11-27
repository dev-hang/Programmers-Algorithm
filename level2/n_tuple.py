def n_tuple(s):
    answer = []
    arr = s[2:-2].split('},{')
    arr.sort(key=lambda x:len(x))

    for i in arr:
        j = i.split(',')
        for k in j:
            if int(k) not in answer:
                answer.append(int(k))

    return answer


print(n_tuple("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# result = [2, 1, 3, 4]
print(n_tuple("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# result = [2, 1, 3, 4]
print(n_tuple("{{20,111},{111}}"))
# result = [111, 20]
print(n_tuple("{{123}}"))
# result = [123]
print(n_tuple("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# result = [3, 2, 4, 1]

