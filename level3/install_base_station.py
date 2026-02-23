import math

def install_base_station(n, stations, w):
    answer = 0
    distances = []
    before_end = 0

    for station in stations:
        start, end = max(1, station-w), min(n, station+w)
        if not before_end:
            distances.append(start-1)
            before_end = end
        else:
            distances.append(start-before_end-1)
            before_end = end

    if before_end < n:
        distances.append(n-before_end)

    for distance in distances:
        answer += math.ceil(distance / (w*2+1))

    return answer




print(install_base_station(11, [4, 11], 1)) # result = 3
print(install_base_station(16, [9], 2)) # result = 3