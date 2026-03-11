def express_in_n(N, number):
    answer = -1
    num_list = []

    for i in range(1, 9):
        num_set = set()
        num_set.add(int(str(N) * i))
        for j in range(i-1):
            for a in num_list[j]:
                for b in num_list[-j-1]:
                    num_set.add(a + b)
                    num_set.add(a - b)
                    num_set.add(a * b)
                    if b != 0:
                        num_set.add(a // b)
        if number in num_set:
            return i

        num_list.append(num_set)

    return answer




print(express_in_n(5, 12)) # result = 4
print(express_in_n(2, 11)) # result = 3