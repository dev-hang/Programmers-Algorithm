from collections import deque

def make_same_sum_of_2_queues(queue1, queue2):
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    for i in range(3 * len(queue1)):
        if queue1_sum > queue2_sum:
            x = queue1.popleft()
            queue1_sum -= x
            queue2_sum += x
            queue2.append(x)
        elif queue1_sum < queue2_sum:
            x = queue2.popleft()
            queue2_sum -= x
            queue1_sum += x
            queue1.append(x)
        else:
            return i

    return -1


print(make_same_sum_of_2_queues([3, 2, 7, 2], [4, 6, 5, 1])) # result = 2
print(make_same_sum_of_2_queues([1, 2, 1, 2], [1, 10, 1, 2])) # result = 7
print(make_same_sum_of_2_queues([1, 1], [1, 5])) # result = -1