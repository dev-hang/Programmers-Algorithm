import heapq

def disk_controller(jobs):
    answer = 0
    time, i, start = 0, 0, -1
    hq = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(hq, [job[1], job[0]])

        if hq:
            cur = heapq.heappop(hq)
            start = time
            time += cur[0]
            answer += time - cur[1]
            i += 1
        else:
            time += 1

    return answer//len(jobs)


print(disk_controller([[0, 3], [1, 9], [3, 5]])) # result = 8