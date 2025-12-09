def open_chatting_room(record):
    answer = []
    log = {}
    cmds = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    for data in record:
        cmd, uid, nick = (data.split() + [None])[:3]
        if nick:
            log[uid] = nick

    for data in record:
        cmd, uid, nick = (data.split() + [None])[:3]
        if cmd in cmds:
            answer.append(log[uid] + cmds[cmd])

    return answer



print(open_chatting_room(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]