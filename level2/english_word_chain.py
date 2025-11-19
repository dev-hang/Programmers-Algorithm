def english_word_chain(n, words):
    answer = [0, 0]
    stack = []
    for i in range(len(words)):
        if i > 0:
            if words[i-1][-1] != words[i][0] or words[i] in stack:
                return [i%n+1, i//n+1]
        stack.append(words[i])
    return answer


print(english_word_chain(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# result = [3,3]
print(english_word_chain(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# result = [0,0]
print(english_word_chain(2 ,["hello", "one", "even", "never", "now", "world", "draw"]))
# result = [1,3]