from itertools import product

def vowel_dictionary(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    dic = []

    for i in range(1, 6):
        for ws in list(product(vowel, repeat=i)):
            wd = ''.join(ws)
            dic.append(wd)

    dic.sort()

    return dic.index(word) + 1





print(vowel_dictionary("AAAAE")) # result = 6
print(vowel_dictionary("AAAE")) # result = 10
print(vowel_dictionary("I")) # result = 1563
print(vowel_dictionary("EIO")) # result = 1189