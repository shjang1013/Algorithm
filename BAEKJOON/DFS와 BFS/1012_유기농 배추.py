# 최소의 배추 흰지렁이 마리 수 출력하기 
def DFS(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        
        return True
    
    return False

# 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    # 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        # 가로, 세로
        x, y = map(int, input().split())
        
        graph[y][x] = 1
    
    count = 0
    for i in range(N):
        for j in range(M):
            if DFS(i, j) == True:
                count += 1

    print(count)

