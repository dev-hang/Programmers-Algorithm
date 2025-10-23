def calculate_plus_minus(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


print(calculate_plus_minus([4,7,12], [True,False,True]))	# result = 9
print(calculate_plus_minus([1,2,3], [False,False,True]))	# result = 0