from collections import deque


def process(priorities, location):
    answer = 0
    q = deque([p, i] for i, p in enumerate(priorities))
    order = 0
    while q:
        if q[0][0] == max(q)[0]:
            p = q.popleft()
            order += 1
            if p[1] == location:
                return order
        else:
            p = q.popleft()
            q.append(p)

    return answer


print(process([2, 1, 3, 2], 2))  # result = 1
print(process([1, 1, 9, 1, 1, 1], 0))  # result = 5
