from collections import Counter

def star_sequence(a):
    answer = 0
    cnt_arr = Counter(a)

    for num in cnt_arr.keys():
        if cnt_arr[num] <= answer:
            continue
        cnt, i = 0, 0
        while i < len(a)-1:
            if (a[i] != num and a[i+1] != num) or (a[i] == a[i+1]):
                i += 1
                continue
            cnt += 1
            i += 2
        answer = max(answer, cnt)

    return answer * 2



print(star_sequence([0])) # result = 0
print(star_sequence([5,2,3,3,5,3])) # result = 4
print(star_sequence([0,3,3,0,7,2,0,2,2,0])) # result = 8