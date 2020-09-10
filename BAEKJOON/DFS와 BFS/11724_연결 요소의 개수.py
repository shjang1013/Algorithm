# 연결 요소의 개수를 출력하기
import sys
sys.setrecursionlimit(10000)

def DFS(v):
    visited[v] = True
    
    for i in range(1, N+1):
        if not visited[i] and graph[v][i] == 1:
            DFS(i)

N, M = map(int, sys.stdin.readline().split())

graph = [[0] * (N+1) for _ in range(N+1)]

visited = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


count = 0

for i in range(1, N+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
