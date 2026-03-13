def edit_table(n, k, cmd):
    answer = ""
    table = ["O" for _ in range(n)]
    stack = []
    linked = {i: [i - 1, i + 1] for i in range(n)}

    for command in cmd:
        if len(command) > 1:
            c, move = command.split()
        else:
            c = command

        if c == "U":
            for _ in range(int(move)):
                k = linked[k][0]
        elif c == "D":
            for _ in range(int(move)):
                k = linked[k][1]
        elif c == "C":
            pre, nxt = linked[k]
            table[k] = "X"
            stack.append((pre, k, nxt))

            if nxt == n:
                k = linked[k][0]
            else:
                k = linked[k][1]

            if pre == -1:
                linked[nxt][0] = pre
            elif nxt == n:
                linked[pre][1] = nxt
            else:
                linked[nxt][0] = pre
                linked[pre][1] = nxt
        elif c == "Z":
            pre, cur, nxt = stack.pop()
            table[cur] = "O"

            if pre == -1:
                linked[nxt][0] = cur
            elif nxt == n:
                linked[pre][1] = cur
            else:
                linked[pre][1] = cur
                linked[nxt][0] = cur

    answer = "".join(table)

    return answer


print(
    edit_table(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
)  # result = "OOOOXOOO"
print(
    edit_table(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
)  # result = "OOXOXOOO"
