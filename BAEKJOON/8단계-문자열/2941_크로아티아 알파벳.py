# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력하기 
count = 0

word = input()

for i in range(len(word)):
    count += 1
    if word[i] == '=':
        if i-1 != 0 and word[i-1] == 'z' and word[i-2] == 'd':
            count -= 2
        else:
            count -= 1
    elif word[i] == '-':
        count -= 1
    elif word[i] == 'j':
        if i != 0 and (word[i-1] == 'l' or word[i-1] == 'n'):
            count -= 1

print(count)
