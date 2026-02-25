from itertools import permutations

def check_banned(user, banned_user):
    if len(user) == len(banned_user):
        for u, b in zip(user, banned_user):
            if b != '*' and u != b:
                return False
        return True
    else:
        return False

def bad_user(user_id, banned_id):
    answer = []
    n = len(banned_id)

    for cases in permutations(user_id, n):
        flg = True
        for i in range(n):
            if not check_banned(cases[i], banned_id[i]):
                flg = False
        if flg:
            cases = set(cases)
            if cases not in answer:
                answer.append(cases)

    return len(answer)





print(bad_user(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # result = 2
print(bad_user(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # result = 2
print(bad_user(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # result =	3