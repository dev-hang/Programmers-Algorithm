def donut_and_bar_graph(edges):
    answer = [0, 0, 0, 0]
    edge_cnt = {}

    for a, b in edges:
        if a not in edge_cnt:
            edge_cnt[a] = [0, 0]
        if b not in edge_cnt:
            edge_cnt[b] = [0, 0]
        edge_cnt[a][0] += 1
        edge_cnt[b][1] += 1

    for edge, cnt in edge_cnt.items():
        out_cnt, in_cnt = cnt
        if out_cnt >= 2 and in_cnt == 0:
            answer[0] = edge
        elif out_cnt == 0 and in_cnt >= 1:
            answer[2] += 1
        elif out_cnt == 2 and in_cnt >= 2:
            answer[3] += 1

    answer[1] = (edge_cnt[answer[0]][0] - answer[2] - answer[3])

    return answer





print(donut_and_bar_graph([[2, 3], [4, 3], [1, 1], [2, 1]]))
# result = [2, 1, 1, 0]
print(donut_and_bar_graph([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
# result = [4, 0, 1, 2]