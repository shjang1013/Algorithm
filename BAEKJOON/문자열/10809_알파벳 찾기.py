word = input()
alphabet_list = []
count = 0

for i in range(26):
    alphabet_list.append(-1)

# 알파벳 위치 저장
for j in word:
    if alphabet_list[ord(j)-97] == -1:
        alphabet_list[ord(j)-97] = count
    count += 1

# 알파벳 위치 출력
for i in range(26):
    print(alphabet_list[i], end=' ')
