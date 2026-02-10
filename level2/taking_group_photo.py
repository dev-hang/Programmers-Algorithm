from itertools import permutations

def taking_group_photo(n, data):
    answer = 0
    friends = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']

    for p in permutations(friends):
        is_correct = True
        for cond in data:
            a, b, sign, val = cond[0], cond[2], cond[3], int(cond[4])
            diff = abs(p.index(a) - p.index(b)) - 1
            if (sign == '=' and diff != val) or (sign == '<' and diff >= val) or (sign == '>' and diff <= val):
                is_correct = False
                break

        if is_correct:
            answer += 1

    return answer




print(taking_group_photo(2, ["N~F=0", "R~T>2"])) # result = 3648
print(taking_group_photo(2, ["M~C<2", "C~M>1"])) # result = 0