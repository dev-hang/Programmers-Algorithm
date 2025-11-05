def check_personality_type(survey, choices):
    answer = ''
    scores = {'R': 0, 'C': 0, 'J': 0, 'A': 0, 'T': 0, 'F': 0, 'M': 0, 'N': 0}
    types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']

    for sv, choice in zip(survey, choices):
        if 1 <= choice <= 3:
            scores[sv[0]] += choice * 3 % 4
        elif 5 <= choice <= 7:
            scores[sv[1]] += choice - 4

    for i in range(0, len(types) - 1, 2):
        if scores[types[i]] >= scores[types[i + 1]]:
            answer += types[i]
        else:
            answer += types[i + 1]

    return answer




print(check_personality_type(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# result = "TCMA"

print(check_personality_type(["TR", "RT", "TR"], [7, 1, 3]))
# result = "RCJA"