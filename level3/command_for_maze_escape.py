def reachable(cur, end, rest):
    distance = abs(cur[0] - end[0]) + abs(cur[1] - end[1])
    if distance <= rest and (rest-distance) % 2 == 0:
        return True
    return False

def command_for_maze_escape(n, m, x, y, r, c, k):
    answer = 'impossible'
    stack = [('', x, y, k)]

    if not reachable((x,y), (r,c), k):
        return answer

    while stack:
        cmd, cx, cy, ck = stack.pop()

        if ck == 0:
            if cx == r and cy == c:
                return cmd
            continue

        for dx, dy, dcmd in [(-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd')]:
            nx, ny, ncmd = cx + dx, cy + dy, cmd + dcmd
            if 0<nx<=n and 0<ny<=m and reachable((nx, ny), (r, c), ck-1):
                stack.append((ncmd, nx, ny, ck-1))

    return answer


print(command_for_maze_escape(3, 4, 2, 3, 3, 1, 5)) # result = "dllrl"
print(command_for_maze_escape(2, 2, 1, 1, 2, 2, 2)) # result = "dr"
print(command_for_maze_escape(3, 3, 1, 2, 3, 3, 4)) # result = "impossible"