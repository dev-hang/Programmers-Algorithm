def string_compression(s):
    answer = len(s)

    for j in range(1, len(s)//2 + 1):
        result = ''
        cnt = 1
        prev = s[:j]

        for i in range(j, len(s)+1, j):
            if prev == s[i:i+j]:
                cnt += 1
            else:
                if cnt == 1:
                    result += prev
                else:
                    result += str(cnt) + prev
                prev = s[i:i+j]
                cnt = 1

        if cnt == 1:
            result += prev
        else:
            result += str(cnt) + prev

        answer = min(answer, len(result))

    return answer




print(string_compression("aabbaccc")) # result = 7
print(string_compression("ababcdcdababcdcd")) # result = 9
print(string_compression("abcabcdede")) # result = 8
print(string_compression("abcabcabcabcdededededede")) # result = 14
print(string_compression("xababcdcdababcdcd")) # result = 17