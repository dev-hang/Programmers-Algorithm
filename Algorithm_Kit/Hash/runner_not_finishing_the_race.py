def runner_not_finishing_the_race(participant, completion):
    names = {}
    temp = 0

    for nm in participant:
        names[hash(nm)] = nm
        temp += hash(nm)

    for nm in completion:
        temp -= hash(nm)

    return names[temp]





print(runner_not_finishing_the_race(["leo", "kiki", "eden"], ["eden", "kiki"])) # result = "leo"
print(runner_not_finishing_the_race(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) # result = "vinko"
print(runner_not_finishing_the_race(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # result = "mislav"