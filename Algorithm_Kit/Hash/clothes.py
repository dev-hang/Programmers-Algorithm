def solution(clothes):
    answer = 1
    d = {}
    
    for cloth, category in clothes:
        if category not in d:
            d[category] = [cloth]
        else:
            d[category].append(cloth)

    for v in d.values():
        answer *= (len(v) + 1)

    return answer - 1




print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # result = 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # result = 3