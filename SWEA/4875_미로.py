# 문제
# SWEA 4875 - [파이썬 S/W 문제해결 기본 5일차] Stack2 - 미로

# 나의 코드
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def safe(y, x):
    return 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3)


def DFS(s_y, s_x):
    global result
    if maze[s_y][s_x] == 3:
        result = 1
        return
    visited.append((s_y, s_x))
    for i in range(4):
        new_y = s_y + dy[i]
        new_x = s_x + dx[i]
        if safe(new_y, new_x) and (new_y, new_x) not in visited:
            DFS(new_y, new_x)


T = int(input())

for tc in range(T):
    N = int(input())
    
    maze = [(list(map(int, input()))) for _ in range(N)]
    s_y = 0
    s_x = 0
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                s_y, s_x = y, x

    result = 0
    visited = []
    DFS(s_y, s_x)
    print("#%d %d" % (tc+1, result))
