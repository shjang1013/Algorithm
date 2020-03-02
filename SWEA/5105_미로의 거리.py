# 문제
# SWEA 5105 - [파이썬 S/W 문제해결 기본 6일차] Queue - 미로의 거리

# 나의 코드
dy = [-1, 1, 0, 0]  # 이동할 수 있는 방향 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]

def availableMaze(y,x):
    return 0 <= y < N and 0 <= x < N and maze[y][x] != 1

def BFS(y, x):
    global result
    
    # 시작점 (y, x)를 큐에 삽입
    queue.append((y, x))
    visited.append((y, x))
    
    # 큐가 비어 있지 않은 경우
    while queue:
        y, x = queue.pop(0)
        
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            
            if availableMaze(new_y, new_x) and (new_y, new_x) not in visited:
                queue.append((new_y, new_x))
                visited.append((new_y, new_x))
                distance[new_y][new_x] = distance[y][x] + 1
                # 도착지점 
                if maze[new_y][new_x] == 3:
                    result = distance[new_y][new_x] - 1
                    return

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
    queue = []
    visited = []
    distance = [[0]*N for _ in range(N)]
    BFS(y, x)
    
    print("#%d %d" %(tc+1, result))

