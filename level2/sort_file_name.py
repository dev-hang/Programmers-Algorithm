def sort_file_name(files):
    answer = []
    d = {}
    st, ed = 0, 0

    for file in files:
        for i in range(1, len(file)):
            if file[i-1].isdigit() != file[i].isdigit():
                if file[i].isdigit():
                    st = i
                else:
                    ed = i - 1
                    break
            ed = len(file) - 1
        d[file] = [file[:st].lower(), int(file[st:ed + 1])]

    answer = [key[0] for key in sorted(d.items(), key=lambda x: (x[1][0], x[1][1]))]

    return answer





print(sort_file_name(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# result = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(sort_file_name(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# result = ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]



