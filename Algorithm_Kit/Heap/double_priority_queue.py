import heapq

def double_priority_queue(operations):
    answer = [0, 0]
    hq = []

    for op in operations:
        cmd, num = op.split()
        if cmd == 'I':
            heapq.heappush(hq, int(num))
        elif cmd == 'D':
            if hq:
                if num == '-1':
                    heapq.heappop(hq)
                else:
                    hq.pop(-1)
        hq.sort()

    if hq:
        answer = [hq[-1], hq[0]]

    return answer





print(double_priority_queue(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # result = [0,0]
print(double_priority_queue(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # result = [333, -45]