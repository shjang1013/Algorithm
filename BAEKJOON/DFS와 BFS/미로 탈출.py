# 최소 이동 칸의 개수를 출력하기
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def BFS(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([])
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 괴물이 있는 부분 무시
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하 경우에만 최단 거리 기록는
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N-1][M-1]

# BFS를 수행한 결과 출력
print(BFS(0, 0))

