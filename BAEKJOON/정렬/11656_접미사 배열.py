# S의 접미사를 사전순으로 한 줄에 하나씩 출력하기
array = []

S = input()

for i in range(len(S)):
    array.append(S[i:])

array.sort()

print('\n'.join(array))
