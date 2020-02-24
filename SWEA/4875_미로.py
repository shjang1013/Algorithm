# 문제
# SWEA 4875 - [파이썬 S/W 문제해결 기본 5일차] Stack2 - 미로

# 나의 코드
dy = [-1, 1, 0, 0]  # 이동할 수 있는 방향 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]

# 미로를 벗어나지 않는 경우와 maze[y][x]이 1이 아닌 경우(벽)
def availableMaze(y,x):
    return 0 <= y < N and 0 <= x < N and maze[y][x] != 1

# 백트래킹
def Backtracking(y, x):
    global result
    
    # 방문한 위치 스택에 push
    visited.append((y,x))
    
    # 도착 위치
    if maze[y][x] == 3:
        result = 1
        return
    
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        
        if availableMaze(new_y, new_x) and (new_y, new_x) not in visited:
            Backtracking(new_y, new_x)


T = int(input())

for tc in range(T):
    N = int(input())
    maze = []
    
    # 2차원 배열 입력 받기
    for i in range(N):
        maze.append(list(map(int, input())))
        # 출발 위치 찾기
        for j in range(N):
            if maze[i][j] == 2:
                x, y = j, i

    result = 0
    visited = []
    
    # 백트래킹
    Backtracking(y, x)
    
    print('#%d %d' %(tc+1, result))
