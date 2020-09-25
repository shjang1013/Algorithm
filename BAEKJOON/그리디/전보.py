import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
N, M, C = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(1, N+1)]

distance = [INF] * (N+1)

# 모든 간선 정보를 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라 알고리즘 정의
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
    
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(C)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
MAX = 0

for i in distance:
    if i != INF:
        count += 1
        MAX = max(MAX, i)

# 시작 노드는 제외해야 하므로 count-1을 출력
print(count-1, MAX)


