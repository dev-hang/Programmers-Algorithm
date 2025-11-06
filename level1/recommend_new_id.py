def recommend_new_id(new_id):
    new_id = new_id.lower()

    for c in '~!@#$%^&*()=+[{]}:?,<>/':
        new_id = new_id.replace(c, '')

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    while new_id[0] == '.' or new_id[-1] == '.':
        if len(new_id) > 1:
            if new_id[0] == '.':
                new_id = new_id[1:]
            if new_id[-1] == '.':
                new_id = new_id[:-1]
        else:
            new_id = ''
            break

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id


print(recommend_new_id("...!@BaT#*..y.abcdefghijklm")) # result = "bat.y.abcdefghi"
print(recommend_new_id("z-+.^."))	# result = "z--"
print(recommend_new_id("=.="))	# result = "aaa"
print(recommend_new_id("123_.def"))	# result = "123_.def"
print(recommend_new_id("abcdefghijklmn.p"))	# result = "abcdefghijklmn"