def cache(cacheSize, cities):
    answer = 0
    hit = []

    for city in cities:
        city = city.lower()

        if city in hit:
            answer += 1
            hit.remove(city)
        else:
            answer += 5

        hit.append(city)

        if len(hit) > cacheSize:
            hit.pop(0)

    return answer


print(cache(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# result = 50
print(cache(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# result = 21
print(cache(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# result = 60
print(cache(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# result = 52
print(cache(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# result = 16
print(cache(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# result = 25


