import re

def news_clustering(str1, str2):
    answer = 0
    str1, str2 = str1.upper(), str2.upper()
    p = re.compile('[A-Z]{2}')

    arr1 = [str1[i:i + 2] for i in range(len(str1) - 1) if p.match(str1[i:i + 2])]
    arr2 = [str2[i:i + 2] for i in range(len(str2) - 1) if p.match(str2[i:i + 2])]

    uno = set(arr1) | set(arr2)
    its = set(arr1) & set(arr2)

    uno_sum, its_sum = 0, 0

    uno_sum = sum([max(arr1.count(w), arr2.count(w)) for w in uno])
    its_sum = sum([min(arr1.count(w), arr2.count(w)) for w in its])

    if uno_sum == 0 and its_sum == 0:
        return 65536

    answer = its_sum / uno_sum

    return int(answer * 65536)


print(news_clustering('FRANCE', 'french')) # result = 16384
print(news_clustering('handshake', 'shake hands')) # result = 65536
print(news_clustering('aa1+aa2', 'AAAA12')) # result = 43690
print(news_clustering('E=M*C^2', 'e=m*c^2')) # result = 65536





