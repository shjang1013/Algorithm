# 나이트가 이동할 수 있는 경우의 수를 출력하기(8가지 방향에 대해 이동 가능한지)
S = input()

x = int(S[1])

y = int(ord(S[0])) - int(ord('a')) + 1

move = [(-2, -1), (-2, 1), (1, -2), (-1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]

count = 0

for i in move:
    nx = x + i[0]
    ny = y + i[1]
    
    if nx >=1 and nx <= 8 and ny >= 1 and ny >= 1 and ny <= 8:
        count += 1

print(count)
