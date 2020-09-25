# 전형적인 플로이드 워셜 알고리즘
# 1번 노드에서 X를 거쳐 K로 가는 최단 거리 구하기

import sys

input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 최종 목적지 노드 K와 거쳐 갈 노드 X를 입력받기
X, K = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print(-1)
else:
    print(distance)
