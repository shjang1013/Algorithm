# 그룹 단어 : 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
T = int(input())
count = 0
for _ in range(T):
    word = input()
    stack = []
    prev = ''
    for i in word:
        # 그룹 단어가 아닐 경우
        if prev != i and i in stack:
            count += 1
            break
        else:
            prev = i
            stack.append(i)

# 모든 단어에서 그룹 단어가 아닐 경우를 제외한다
print(T - count)

# find를 이용한 풀이
T = int(input())
count = 0

for _ in range(T):
    word = input()
    if list(word) == sorted(word, key=word.find):
        count += 1

print(count)
