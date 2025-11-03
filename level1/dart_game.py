def dart_game(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    scores = ['10' if i == 'k' else i for i in dartResult]
    bonus = {'S': 1, 'D': 2, 'T': 3}

    i = -1
    for score in scores:
        if score in bonus:
            answer[i] = answer[i] ** bonus[score]
        elif score == '*':
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i - 1] = answer[i - 1] * 2
        elif score == '#':
            answer[i] = answer[i] * -1
        else:
            answer.append(int(score))
            i += 1

    return sum(answer)




print(dart_game('1S2D*3T')) # result = 37
print(dart_game('1D2S#10S')) # result = 9
print(dart_game('1D2S0T')) # result = 3
print(dart_game('1S*2T*3S')) # result = 23
print(dart_game('1D#2S*3S')) # result = 5
print(dart_game('1T2D3D#')) # result = -4
print(dart_game('1D2S3T*')) # result = 59