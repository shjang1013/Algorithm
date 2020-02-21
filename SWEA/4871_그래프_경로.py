# 문제
# SWEA 4871 - [파이썬 S/W 문제해결 기본 4일차] Stack1 - 그래프 경로

# 나의 코드
def DFS(S):
    # 결과값
    global result
    
    # S 방문했으므로 visited[S] <- true
    visited[S] = 1
    for i in range(1, V+1):
        # S의 인접 정점 중 방문 안한 정점 찾기
        if Map[S][i] and not visited[i]:
            # i가 마지막 정점과 같다면
            if i == G:
                result = 1
                return
            # i가 마지막 정점과 같지 않다면 DFS 반복
            DFS(i)

T = int(input())

for tc in range(T):
    # V : 정점, E : 간선
    V, E = map(int, input().split())
    
    # 초기화
    Map = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    
    # 간선이 있을 경우 Map[s][e] <- true
    for i in range(E):
        s, e = map(int, input().split())
        Map[s][e] = 1
    
    # S : 출발정점, G : 도착정점 
    S, G = map(int, input().split())
    result = 0
    
    # DFS 구현
    DFS(S)
    print('#%d %d' %(tc+1, result))
