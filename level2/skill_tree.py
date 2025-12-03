def skill_tree(skill, skill_trees):
    answer = 0

    for sk_tree in skill_trees:
        check = ''
        for sk in sk_tree:
            if sk in skill:
                check += sk
        if check == skill[:len(check)]:
            answer += 1

    return answer


print(skill_tree("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # result = 2