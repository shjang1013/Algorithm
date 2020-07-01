# 단어에서 가장 많이 사용된 알파벳 
import collections

word = collections.Counter(input().upper()).most_common()

if len(word) > 1:
    if word[0][1] == word[1][1]:
        print("?")
    else:
        print(word[0][0])
else:
    print(word[0][0])
