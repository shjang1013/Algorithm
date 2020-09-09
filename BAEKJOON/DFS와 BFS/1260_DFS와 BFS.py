from collections import deque

# 
def DFS(v):
    visited[v-1] = True
    print(v, end=' ')
    
    for i in range(len(graph)):
        if not visited[i] and graph[v-1][i] == 1:
            DFS(i+1)

def BFS(start):
    queue = deque([start])
    visited[start-1] = False
    
    while queue:
        v = queue[0]
        print(v, end=' ')
        queue.popleft()
        for i in range(len(graph)):
            if visited[i] and graph[v-1][i]:
                queue.append(i+1)
                visited[i] = False

N, M, v = map(int, input().split())

visited = [0] * N

graph = [[0] * N for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    
    # 양방향
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

DFS(v)
print()
BFS(v)
