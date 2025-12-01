def visit_length(dirs):
    cmd = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    visited = set()

    for d in dirs:
        dx, dy = cmd[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(tuple(sorted([(x, y), (nx, ny)])))
            x, y = nx, ny

    return len(visited)


print(visit_length("ULURRDLLU")) # result = 7
print(visit_length("LULLLLLLU")) # result = 7