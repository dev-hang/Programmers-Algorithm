def num_and_string(s):
    answer = ''
    word = ''
    table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for n in s:
        if n.isalpha():
            word += n
            if word in table:
                answer += str(table.index(word))
                word = ''
        else:
            answer += n

    return int(answer)



print(num_and_string("one4seveneight")) # result = 1478
print(num_and_string("23four5six7")) # result = 234567
print(num_and_string("2three45sixseven")) # result = 234567
print(num_and_string("123")) # result = 123