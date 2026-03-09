def lifeboat(people, limit):
    answer = 0
    start, end = 0, len(people)-1
    people.sort()

    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1

    return answer





print(lifeboat([70, 50, 80, 50], 100)) # result = 3
print(lifeboat([70, 80, 50], 100)) # result = 3