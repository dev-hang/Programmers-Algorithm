from collections import deque

def word_conversion(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    q = deque([[begin, 0]])

    while q:
        cur, lev = q.popleft()

        if cur == target:
            return lev

        for word in words:
            cnt = 0
            for w1, w2 in zip(cur, word):
                if w1 == w2:
                    cnt += 1
            if cnt == len(cur) - 1:
                q.append([word, lev + 1])

    return answer




print(word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # result = 4
print(word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # result = 0