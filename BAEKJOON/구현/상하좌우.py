# 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하기
import sys

N = int(input())

plan = list(sys.stdin.readline().split())

x = y = 1

for i in plan:
    if i == 'L':    # 좌
        if x <= 1:
            continue
        x -= 1
    elif i == 'R':  # 우
        if x >= N:
            continue
        x += 1
    elif i == 'U':  # 상
        if y <= 1:
            continue
        y -= 1
    elif i == 'D':  # 하
        if y >= N:
            continue
        y += 1

print(y, x)


# 다른 코드
N = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(4):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    
    x, y = nx, ny
