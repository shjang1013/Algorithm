# 문제
# SWEA 5102 - [파이썬 S/W 문제해결 기본 6일차] Queue - 노드의 거리

# 나의 코드
def BFS(S):
    global result
    queue = []
    queue.append(S)
    visited[S] = 1
    distance[S] = 0
    
    while queue:
        t = queue.pop(0)
        for i in range(1, V+1):
            # t와 연결된 모든 선에 대해
            if graph[t][i] and not visited[i]:
                queue.append(i)
                distance[i] = distance[t] + 1
                
                # 도착정점일 경우
                if i == G:
                    result = distance[i]
                    return
    # 간선이 연결되지 않은 경우
    return


T = int(input())

for tc in range(T):
    # V : 정점, E : 간선
    V, E = map(int, input().split())
    
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = distance = [0]*(V+1)
    
    # 무방향 그래프
    for i in range(E):
        s, e = map(int, input().split())
        graph[s][e] = 1
        graph[e][s] = 1

    # S: 출발정점, G: 도착정점
    S, G = map(int, input().split())

    result = 0
    
    # BFS 구현
    BFS(S)
    
    print("#%d %d" %(tc+1, result))

