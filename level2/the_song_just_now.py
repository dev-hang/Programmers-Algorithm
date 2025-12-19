def the_song_just_now(m, musicinfos):
    answer = '(None)'
    order = 0    
    m = m.replace('C#','1').replace('D#','2').replace('E#','3').replace('F#','4').replace('G#','5').replace('A#','6').replace('B#','7')
    
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        time = end - start
        
        music = music.replace('C#','1').replace('D#','2').replace('E#','3').replace('F#','4').replace('G#','5').replace('A#','6').replace('B#','7')
        
        music = (music * time)[:time]

        if m in music:
            if answer != 'None':
                if order >= time:
                    continue
            answer = title
            order = time
            
    return answer




print(the_song_just_now("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # result = "HELLO"
print(the_song_just_now("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) # result = "FOO"
print(the_song_just_now("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # result = "WORLD"