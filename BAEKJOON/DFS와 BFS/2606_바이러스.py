import sys
sys.setrecursionlimit(10000)

def DFS(v):
    visited[v] = True
    
    global count
    
    for i in range(len(graph)):
        if not visited[i] and graph[v][i] == 1:
            count += 1
            DFS(i)

N = int(input())
M = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]

visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    
    graph[x][y] = 1
    graph[y][x] = 1

count = 0

DFS(1)

print(count)
