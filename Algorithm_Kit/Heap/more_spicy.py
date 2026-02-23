import heapq

def more_spicy(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        idx = heapq.heappop(scoville)
        if idx < K:
            idx += heapq.heappop(scoville) * 2
            heapq.heappush(scoville, idx)
            answer += 1
        else:
            return answer

    if scoville and heapq.heappop(scoville) >= K:
        return answer

    return -1



print(more_spicy([1, 2, 3, 9, 10, 12], 7)) # result = 2