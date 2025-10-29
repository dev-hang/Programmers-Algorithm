from itertools import combinations

def sum_of_2_picked(numbers):
    answer = []
    combis = list(combinations(numbers, 2))

    for combi in combis:
        sum_combi = sum(combi)

        if sum_combi not in answer:
            answer.append(sum_combi)

    return sorted(answer)


print(sum_of_2_picked([2,1,3,4,1])) # result = [2,3,4,5,6,7]
print(sum_of_2_picked([5,0,2,7])) # result = [2,5,7,9,12]