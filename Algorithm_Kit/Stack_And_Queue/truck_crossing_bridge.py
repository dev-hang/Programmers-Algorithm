from collections import deque

def truck_crossing_bridge(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    total_weight = 0

    while truck_weights:
        answer += 1
        total_weight -= bridge.popleft()

        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            total_weight += truck
            bridge.append(truck)
        else:
            bridge.append(0)

    answer += bridge_length

    return answer





print(truck_crossing_bridge(2, 10, [7,4,5,6])) # result = 8
print(truck_crossing_bridge(100, 100, [10])) # result = 101
print(truck_crossing_bridge(100, 100, [10,10,10,10,10,10,10,10,10,10])) # result = 110