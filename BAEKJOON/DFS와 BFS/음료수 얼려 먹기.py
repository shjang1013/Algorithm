# 아이스크림 개수 출력하기 
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# DFS로 툭정한 노드를 방문한 뒤에 연결된 모든 노드들도 방
def DFS(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 => 따로 visited를 만들지 않고 graph에서 방문 처리 함
        graph[x][y] = 1
        
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0

for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if DFS(i, j) == True:
            result += 1

print(result)
