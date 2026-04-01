answer = []
table = [['' for _ in range(51)] for _ in range(51)]
P = [[(r, c) for c in range(51)] for r in range(51)]

def find(r, c):
    while (r, c) != P[r][c]:
        r, c = P[r][c]
    return r, c

def union(r1, c1, r2, c2):
    P[r2][c2] = P[r1][c1]

def update_cell(r, c, v):
    r, c = find(r, c)
    table[r][c] = v

def update_value(v1, v2):
    for i in range(51):
        for j in range(51):
            if table[i][j] == v1:
                table[i][j] = v2

def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)

    if r1 == r2 and c1 == c2:
        return

    if table[r1][c1]:
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)

def unmerge(r, c):
    pr, pc = find(r, c)
    value = table[pr][pc]
    arr = []

    for i in range(51):
        for j in range(51):
            if find(i, j) == (pr, pc):
                arr.append((i, j))

    for i, j in arr:
        P[i][j] = (i, j)
        table[i][j] = ''

    table[r][c] = value

def print_cell(r, c):
    r, c = find(r, c)
    answer.append(table[r][c]) if table[r][c] else answer.append('EMPTY')

def solution(commands):
    for cmd in commands:
        cmds = cmd.split()
        if cmds[0] == 'UPDATE':
            if len(cmds) == 4:
                cmd, r, c, v = cmds
                update_cell(int(r), int(c), v)
            elif len(cmds) == 3:
                cmd, v1, v2 = cmds
                update_value(v1, v2)
        elif cmds[0] == 'MERGE':
            cmd, r1, c1, r2, c2 = cmds
            merge(int(r1), int(c1), int(r2), int(c2))
        elif cmds[0] == 'UNMERGE':
            cmd, r, c = cmds
            unmerge(int(r), int(c))
        elif cmds[0] == 'PRINT':
            cmd, r, c = cmds
            print_cell(int(r), int(c))

    return answer


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# result = ["EMPTY", "group"]
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
# result = ["d", "EMPTY"]