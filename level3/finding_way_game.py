import sys

sys.setrecursionlimit(10 ** 7)

def insert(tree, node, parent_idx):
    idx, x, y = node
    (p_x, p_y), left, right = tree[parent_idx]

    if p_x < x:
        if right != 0:
            insert(tree, node, right)
        else:
            tree[parent_idx][2] = idx
            tree[idx] = [(x, y), 0, 0]
    else:
        if left != 0:
            insert(tree, node, left)
        else:
            tree[parent_idx][1] = idx
            tree[idx] = [(x, y), 0, 0]


def post_order(tree, node_idx):
    path = []

    if node_idx == 0:
        return path

    path += post_order(tree, tree[node_idx][1])
    path += post_order(tree, tree[node_idx][2])
    path.append(node_idx)

    return path


def pre_order(tree, node_idx):
    path = []

    if node_idx == 0:
        return path

    path.append(node_idx)
    path += pre_order(tree, tree[node_idx][1])
    path += pre_order(tree, tree[node_idx][2])

    return path


def finding_way_game(nodeinfo):
    sorted_node_info = []

    for idx, [x, y] in enumerate(nodeinfo, 1):
        sorted_node_info.append([idx, x, y])
    sorted_node_info.sort(key=lambda x: x[2])

    tree = dict()
    root_idx, root_x, root_y = sorted_node_info.pop()
    tree[root_idx] = [(root_x, root_y), 0, 0]

    while sorted_node_info:
        node = sorted_node_info.pop()
        insert(tree, node, root_idx)

    answer = [pre_order(tree, root_idx), post_order(tree, root_idx)]

    return answer

print(finding_way_game([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]